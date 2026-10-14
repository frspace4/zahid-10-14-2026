# -*- coding: utf-8 -*-

import os
import json
import time
import asyncio
import hashlib
import secrets
import contextvars
from typing import Dict, Any

from aiohttp import web

import dashboard_server as ds

bot_state = ds.bot_state

from templates import (
    LOGIN_HTML,
    PLANS_HTML,
    DASHBOARD_HTML,
    EXPIRED_HTML,
    ADMIN_LOGIN_HTML,
    ADMIN_PANEL_HTML,
    HOME_HTML,
)

ADMIN_USERNAME = "hh"
ADMIN_PASSWORD = "hh"
ADMIN_PATH = "/admin/hh/levelup/adm-dash"

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
SESSIONS_FILE = os.path.join(DATA_DIR, "sessions.json")

SESSION_COOKIE = "vxl_session"
SESSION_TTL = 7 * 24 * 3600

USER_WORKERS: Dict[str, Dict[str, asyncio.Task]] = {}
USER_PAUSED: Dict[str, set] = {}
USER_DELETED: Dict[str, set] = {}
_LAST_SYNC: Dict[str, float] = {}
_CURRENT_OWNER = contextvars.ContextVar("current_owner", default=None)
USER_STATUS: Dict[str, Dict[str, str]] = {}
USER_RETRIES: Dict[str, Dict[str, int]] = {}
USER_QUEUE_LOCK: Dict[str, asyncio.Lock] = {}

DEFAULT_SETTINGS = {
    "daily_autoplay": False,
    "days": 1,
    "active_slots": 10,
    "login_retry": 3,
    "daily_limit": 60000,
    "all_bots": True,
    "target_delete": False,
    "exp_limit": 0,
    "level_limit": 21,
    "game_mode": "AUTO"
}

def get_user_settings(u: dict) -> dict:
    s = dict(DEFAULT_SETTINGS)
    if isinstance(u, dict):
        user_s = u.get("settings", {})
        if isinstance(user_s, dict):
            s.update(user_s)
        if "active_slots" not in user_s and u.get("slots"):
            try:
                s["active_slots"] = int(u.get("slots"))
            except Exception:
                pass
    return s

def format_duration(seconds: int) -> str:
    if seconds <= 0:
        return "0m"
    hours = seconds // 3600
    mins = (seconds % 3600) // 60
    days = hours // 24
    if days > 0:
        return f"{days}d {hours % 24}h"
    if hours > 0:
        return f"{hours}h {mins}m"
    return f"{max(1, mins)}m"

def compute_account_eta(acc: dict, settings: dict) -> tuple:
    exp_target = int(settings.get("exp_limit", 0) or 0)
    level_target = int(settings.get("level_limit", 0) or 0)
    gained = int(acc.get("gained_exp", 0) or 0)
    cur_level = int(acc.get("level", 1) or 1)

    if exp_target <= 0 and level_target <= 0:
        return None, "--", 0

    # If either target is reached, account is completed
    is_done = False
    if exp_target > 0 and gained >= exp_target:
        is_done = True
    if level_target > 0 and cur_level >= level_target:
        is_done = True

    if is_done:
        return 0, "DONE", 100

    # Compute remaining work and progress pct for each active target
    exp_rem = max(0, exp_target - gained) if exp_target > 0 else None
    exp_pct = min(100, int((gained / exp_target) * 100)) if exp_target > 0 else 0

    lvl_needed = max(0, level_target - cur_level) if level_target > 0 else None
    lvl_rem = (lvl_needed * 8000) if level_target > 0 else None
    lvl_pct = min(100, int((cur_level / level_target) * 100)) if level_target > 0 else 0

    if exp_rem is not None and lvl_rem is not None:
        remaining = min(exp_rem, lvl_rem)
        pct = max(exp_pct, lvl_pct)
    elif exp_rem is not None:
        remaining = exp_rem
        pct = exp_pct
    else:
        remaining = lvl_rem
        pct = lvl_pct

    created_at = acc.get("created_at") or (time.time() - 300)
    elapsed = max(60.0, time.time() - created_at)
    if gained > 50:
        rate = gained / elapsed
    else:
        rate = 2.08

    eta_sec = int(remaining / max(0.1, rate))
    return eta_sec, format_duration(eta_sec), pct

def compute_total_eta(accounts: list, settings: dict) -> tuple:
    exp_target = int(settings.get("exp_limit", 0) or 0)
    level_target = int(settings.get("level_limit", 0) or 0)
    active_slots = max(1, int(settings.get("active_slots", 10) or 10))

    if exp_target <= 0 and level_target <= 0:
        return None, "No target set"

    total_remaining = 0
    for a in accounts:
        if a.get("status") in ("DONE", "DELETED"):
            continue
        gained = int(a.get("gained_exp", 0) or 0)
        cur_level = int(a.get("level", 1) or 1)

        # Skip accounts that reached either target
        if exp_target > 0 and gained >= exp_target:
            continue
        if level_target > 0 and cur_level >= level_target:
            continue

        if exp_target > 0 and level_target > 0:
            exp_rem = max(0, exp_target - gained)
            lvl_rem = max(0, (level_target - cur_level) * 8000)
            total_remaining += min(exp_rem, lvl_rem)
        elif exp_target > 0:
            total_remaining += max(0, exp_target - gained)
        elif level_target > 0:
            total_remaining += max(0, (level_target - cur_level) * 8000)

    if total_remaining <= 0:
        return 0, "Completed"

    total_rate = active_slots * 2.08
    total_sec = int(total_remaining / total_rate)
    return total_sec, format_duration(total_sec)


async def sync_user_accounts_to_disk(username):
    """Persist live bot_state account data into users.json so logout/login doesn't lose progress."""
    try:
        users = load_users()
        u = users.get(username)
        if not u:
            return
        accounts = u.get("accounts", [])
        if not accounts:
            return
        changed = False
        for saved in accounts:
            saved_key = str(saved.get("uid")) if saved.get("type") == "guest" else str(saved.get("token", ""))[:20]
            live = None
            for uid, acc in ds.bot_state.accounts.items():
                if acc.get("_owner") != username:
                    continue
                if str(uid) == saved_key:
                    live = acc
                    break
                cred = ds.bot_state.account_credentials.get(str(uid))
                if cred:
                    if saved.get("type") == "guest" and str(cred.get("auth_uid")) == saved_key:
                        live = acc
                        break
                    if saved.get("type") == "token" and str(cred.get("auth_token", ""))[:20] == saved_key:
                        live = acc
                        break
            if not live:
                continue
            if saved.get("initial_exp") is None and live.get("initial_exp") is not None:
                saved["initial_exp"] = live["initial_exp"]
                changed = True
            new_last_exp = live.get("current_exp")
            if new_last_exp is not None and saved.get("last_exp") != new_last_exp:
                saved["last_exp"] = new_last_exp
                changed = True
            new_level = live.get("level")
            if new_level is not None and saved.get("last_level") != new_level:
                saved["last_level"] = new_level
                changed = True
            new_nick = live.get("nickname")
            if new_nick and saved.get("last_nickname") != new_nick:
                saved["last_nickname"] = new_nick
                changed = True
            new_region = live.get("region")
            if new_region and saved.get("last_region") != new_region:
                saved["last_region"] = new_region
                changed = True
            new_gained = live.get("gained_exp")
            if new_gained is not None and saved.get("gained_exp") != new_gained:
                saved["gained_exp"] = new_gained
                changed = True
            new_played = live.get("matches_played")
            if new_played is not None and saved.get("matches_played") != new_played:
                saved["matches_played"] = new_played
                changed = True
            if live.get("created_at") and saved.get("created_at") != live.get("created_at"):
                saved["created_at"] = live.get("created_at")
                changed = True
            saved["last_update"] = time.time()
            changed = True
        if changed:
            save_users(users)
    except Exception as e:
        print(f"[auth] sync_user_accounts_to_disk error for {username}: {e}", flush=True)


def _ensure():
    os.makedirs(DATA_DIR, exist_ok=True)


def _read(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def _write(path, data):
    _ensure()
    tmp = f"{path}.{os.getpid()}_{time.time_ns()}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    for _ in range(10):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            time.sleep(0.05)
        except Exception:
            break
    try:
        os.replace(tmp, path)
    except Exception:
        # Fallback direct write
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            if os.path.exists(tmp):
                os.remove(tmp)
        except Exception:
            pass


def load_users():
    return _read(USERS_FILE, {})


def save_users(u):
    _write(USERS_FILE, u)


def load_sessions():
    return _read(SESSIONS_FILE, {})


def save_sessions(s):
    _write(SESSIONS_FILE, s)


def hash_pw(pw, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt.encode(), 120000)
    return h.hex(), salt


def verify_pw(pw, h, salt):
    hh, _ = hash_pw(pw, salt)
    return secrets.compare_digest(hh, h)


def create_session(username, is_admin=False):
    token = secrets.token_urlsafe(32)
    s = load_sessions()
    now = time.time()
    s[token] = {"username": username, "is_admin": is_admin, "created_at": now, "expires_at": now + SESSION_TTL}
    now_ts = time.time()
    s = {k: v for k, v in s.items() if v.get("expires_at", 0) > now_ts}
    save_sessions(s)
    return token


def get_session(token):
    if not token:
        return None
    s = load_sessions()
    v = s.get(token)
    if not v:
        return None
    if time.time() > v.get("expires_at", 0):
        s.pop(token, None)
        save_sessions(s)
        return None
    return v


def destroy_session(token):
    s = load_sessions()
    s.pop(token, None)
    save_sessions(s)


DEFAULT_USERNAME = "admin"


def ensure_default_user():
    users = load_users()
    now = time.time()
    perpetual_time = now + 100 * 365 * 86400

    target_un = DEFAULT_USERNAME
    changed = False

    if target_un not in users:
        # Check for legacy user (e.g. 'zahid') to migrate accounts and settings
        legacy_cand = None
        if "zahid" in users:
            legacy_cand = "zahid"
        else:
            for un in users.keys():
                if not un.startswith("test_"):
                    legacy_cand = un
                    break
        if legacy_cand and legacy_cand in users:
            legacy_u = users[legacy_cand]
            users[target_un] = {
                "password_hash": "",
                "salt": "",
                "slots": legacy_u.get("slots", 10),
                "plan_hours": 999999,
                "created_at": legacy_u.get("created_at", now),
                "expires_at": perpetual_time,
                "accounts": list(legacy_u.get("accounts", [])),
                "_expired_flag": False,
                "settings": dict(legacy_u.get("settings", DEFAULT_SETTINGS)),
            }
            changed = True
        else:
            users[target_un] = {
                "password_hash": "",
                "salt": "",
                "slots": 10,
                "plan_hours": 999999,
                "created_at": now,
                "expires_at": perpetual_time,
                "accounts": [],
                "_expired_flag": False,
                "settings": dict(DEFAULT_SETTINGS),
            }
            changed = True
    else:
        u = users[target_un]
        # Consolidate legacy accounts if another non-test user exists
        for leg_un in list(users.keys()):
            if leg_un != target_un and not leg_un.startswith("test_"):
                leg_accs = users[leg_un].get("accounts", [])
                if leg_accs:
                    existing_keys = {
                        str(a.get("uid") if a.get("type") == "guest" else a.get("token", "")[:20])
                        for a in u.get("accounts", [])
                    }
                    for a in leg_accs:
                        k = str(a.get("uid") if a.get("type") == "guest" else a.get("token", "")[:20])
                        if k not in existing_keys:
                            u.setdefault("accounts", []).append(a)
                            existing_keys.add(k)
                    users[leg_un]["accounts"] = []
                    changed = True
        if u.get("expires_at", 0) < now + 30 * 86400:
            u["expires_at"] = perpetual_time
            changed = True
        if u.get("_expired_flag", False):
            u["_expired_flag"] = False
            changed = True
        if "settings" not in u:
            u["settings"] = dict(DEFAULT_SETTINGS)
            changed = True

    if changed:
        save_users(users)
    return target_un


def ensure_user_exists(un=None):
    if not un or un == DEFAULT_USERNAME:
        return ensure_default_user()
    users = load_users()
    now = time.time()
    perpetual_time = now + 100 * 365 * 86400
    if un not in users:
        users[un] = {
            "password_hash": "",
            "salt": "",
            "slots": 10,
            "plan_hours": 999999,
            "created_at": now,
            "expires_at": perpetual_time,
            "accounts": [],
            "_expired_flag": False,
            "settings": dict(DEFAULT_SETTINGS),
        }
        save_users(users)
    return un


def get_effective_user(un: str) -> str:
    if un and un.startswith("test_"):
        return un
    return DEFAULT_USERNAME


def cur_user(req):
    ck = None
    if hasattr(req, "cookies") and req.cookies:
        ck = req.cookies.get(SESSION_COOKIE)
    if ck:
        s = get_session(ck)
        if s:
            return s
    return None


def cur_admin(req):
    s = cur_user(req)
    if s and s.get("is_admin", True):
        return s
    return None


def _set_ck(resp, token):
    resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL, httponly=True, samesite="Lax", path="/")


def _clr_ck(resp):
    resp.del_cookie(SESSION_COOKIE, path="/")


_orig_register = ds.BotState.register_account


def _patched_register(self, uid, nickname, region, level, exp, likes=0, **kwargs):
    uid_str = str(uid)
    owner = _CURRENT_OWNER.get()

    if owner is None:
        try:
            for un, udata in load_users().items():
                for acc in udata.get("accounts", []):
                    if acc.get("type") == "guest":
                        acc_uid = str(acc.get("uid", ""))
                    else:
                        acc_uid = str(acc.get("token", ""))[:20]
                    if acc_uid == uid_str:
                        owner = un
                        break
                if owner:
                    break
        except Exception:
            pass

    if owner:
        deleted = USER_DELETED.get(owner, set())
        paused = USER_PAUSED.get(owner, set())
        if uid_str in deleted or uid_str in paused:
            return

    saved_initial = None
    saved_matches = 0
    saved_created = None
    if owner:
        try:
            users = load_users()
            u = users.get(owner)
            if u:
                for saved in u.get("accounts", []):
                    saved_key = str(saved.get("uid")) if saved.get("type") == "guest" else str(saved.get("token", ""))[:20]
                    if saved_key == uid_str:
                        saved_initial = saved.get("initial_exp")
                        saved_matches = saved.get("matches_played", 0)
                        saved_created = saved.get("created_at")
                        break
        except Exception:
            pass

    is_new = uid_str not in self.accounts
    _orig_register(self, uid, nickname, region, level, exp, likes, **kwargs)
    acc = self.accounts.get(uid_str)
    if not acc:
        return

    if saved_initial is not None:
        acc["initial_exp"] = saved_initial
        acc["gained_exp"] = max(0, exp - saved_initial)
    if saved_matches > 0:
        acc["matches_played"] = saved_matches
    if saved_created:
        acc["created_at"] = saved_created

    if owner:
        acc["_owner"] = owner

    if is_new and "created_at" not in acc:
        acc["created_at"] = time.time()

    acc["last_update"] = time.time()

    if owner:
        try:
            users = load_users()
            u = users.get(owner)
            if u:
                for saved in u.get("accounts", []):
                    saved_key = str(saved.get("uid")) if saved.get("type") == "guest" else str(saved.get("token", ""))[:20]
                    if saved_key == uid_str:
                        if saved.get("initial_exp") is None:
                            saved["initial_exp"] = acc["initial_exp"]
                        saved["last_exp"] = acc["current_exp"]
                        saved["last_level"] = acc["level"]
                        saved["last_nickname"] = acc["nickname"]
                        saved["last_region"] = acc["region"]
                        saved["last_mode"] = acc.get("mode", "BR")
                        saved["gained_exp"] = acc["gained_exp"]
                        saved["matches_played"] = acc["matches_played"]
                        saved["created_at"] = acc.get("created_at")
                        saved["last_update"] = time.time()
                        break
                save_users(users)
        except Exception:
            pass


ds.BotState.register_account = _patched_register


async def stop_user_workers(username):
    workers = USER_WORKERS.pop(username, {})
    tasks = list(workers.values())
    for t in tasks:
        try:
            if not t.done():
                t.cancel()
        except (RuntimeError, Exception):
            pass
    if tasks:
        try:
            await asyncio.gather(*tasks, return_exceptions=True)
        except (RuntimeError, Exception):
            pass

    for key in list(bot_state.account_workers.keys()):
        if str(key).startswith(username + "::"):
            t = bot_state.account_workers.pop(key, None)
            if t:
                try:
                    if not t.done():
                        t.cancel()
                    await asyncio.wait_for(t, timeout=3)
                except (asyncio.CancelledError, asyncio.TimeoutError, RuntimeError, Exception):
                    pass

    try:
        await asyncio.sleep(0.2)
    except (RuntimeError, Exception):
        pass


async def sync_user_queue(username: str):
    """
    Queue and active slots concurrency manager.
    Enforces that only up to `active_slots` accounts are running and logged in!
    All other accounts remain in WAITING or OFFLINE state without logging in.
    Also handles target completion, error threshold, and all_bots toggling.
    """
    if username not in USER_QUEUE_LOCK:
        USER_QUEUE_LOCK[username] = asyncio.Lock()

    async with USER_QUEUE_LOCK[username]:
        users = load_users()
        u = users.get(username)
        if not u:
            return
        default_un = ensure_default_user()
        if username != default_un and time.time() >= u.get("expires_at", 0):
            await stop_user_workers(username)
            return

        settings = get_user_settings(u)
        active_slots = max(1, int(settings.get("active_slots", 10)))
        all_bots = bool(settings.get("all_bots", True))
        target_delete = bool(settings.get("target_delete", False))
        exp_limit = int(settings.get("exp_limit", 0))
        level_limit = int(settings.get("level_limit", 0))
        login_retry = int(settings.get("login_retry", 3))
        game_mode = settings.get("game_mode", "AUTO")

        try:
            bot_state.game_mode = game_mode
        except Exception:
            pass

        workers = USER_WORKERS.setdefault(username, {})
        paused = USER_PAUSED.setdefault(username, set())
        deleted = USER_DELETED.setdefault(username, set())
        status_map = USER_STATUS.setdefault(username, {})

        # If all bots are turned OFF:
        if not all_bots:
            for k, t in list(workers.items()):
                if t and not t.done():
                    t.cancel()
            workers.clear()
            for acc in u.get("accounts", []):
                k = str(acc.get("uid") if acc.get("type") == "guest" else acc.get("token", "")[:20])
                if k and k not in deleted:
                    status_map[k] = "PAUSED"
            return

        # When all bots is ON, any account not individually in paused set should be un-paused
        for acc in u.get("accounts", []):
            k = str(acc.get("uid") if acc.get("type") == "guest" else acc.get("token", "")[:20])
            if k and k not in paused and status_map.get(k) == "PAUSED":
                status_map[k] = "WAITING"

        # Check target completions
        accounts_to_keep = []
        user_accounts = u.get("accounts", [])
        changed = False

        for acc in list(user_accounts):
            k = str(acc.get("uid") if acc.get("type") == "guest" else acc.get("token", "")[:20])
            if not k or k in deleted:
                continue

            live_acc = None
            for uid_b, b_acc in ds.bot_state.accounts.items():
                if b_acc.get("_owner") == username and str(uid_b) == k:
                    live_acc = b_acc
                    break
                cred = ds.bot_state.account_credentials.get(str(uid_b))
                if cred:
                    if acc.get("type") == "guest" and str(cred.get("auth_uid")) == k:
                        live_acc = b_acc
                        break
                    if acc.get("type") == "token" and str(cred.get("auth_token", ""))[:20] == k:
                        live_acc = b_acc
                        break

            cur_gained = live_acc.get("gained_exp", acc.get("gained_exp", 0)) if live_acc else acc.get("gained_exp", 0)
            cur_level = live_acc.get("level", acc.get("last_level", 1)) if live_acc else acc.get("last_level", 1)

            is_target_done = False
            if exp_limit > 0 and cur_gained >= exp_limit:
                is_target_done = True
            if level_limit > 0 and cur_level >= level_limit:
                is_target_done = True

            if is_target_done:
                status_map[k] = "DONE"
                t = workers.pop(k, None)
                if t and not t.done():
                    t.cancel()
                if target_delete:
                    deleted.add(k)
                    changed = True
                    ds.bot_state.accounts.pop(k, None)
                    ds.bot_state.log(f"Account {k} reached target! Auto-deleted.", "success", k)
                    continue

            accounts_to_keep.append(acc)

        if changed:
            u["accounts"] = accounts_to_keep
            users[username] = u
            save_users(users)
            user_accounts = accounts_to_keep

        # Prune finished workers
        for k in list(workers.keys()):
            if workers[k].done():
                del workers[k]

        # Determine the target running accounts based on priority order in user_accounts
        desired_running_keys = []
        for acc in user_accounts:
            if len(desired_running_keys) >= active_slots:
                break
            k = str(acc.get("uid") if acc.get("type") == "guest" else acc.get("token", "")[:20])
            if not k or k in deleted or k in paused:
                continue
            cur_st = status_map.get(k, "WAITING")
            if cur_st in ("DONE", "ERROR", "OFFLINE"):
                continue
            desired_running_keys.append(k)

        # Stop workers for accounts that should not be running (e.g. slots reduced or reordered)
        for k in list(workers.keys()):
            if k not in desired_running_keys:
                t = workers.pop(k, None)
                if t and not t.done():
                    t.cancel()
                if status_map.get(k) not in ("DONE", "ERROR", "PAUSED", "OFFLINE"):
                    status_map[k] = "WAITING"

        # Spawn workers for desired accounts that do not have active workers yet
        for acc in user_accounts:
            k = str(acc.get("uid") if acc.get("type") == "guest" else acc.get("token", "")[:20])
            if k in desired_running_keys:
                if k not in workers or workers[k].done():
                    status_map[k] = "RUNNING"
                    if acc.get("type") == "guest":
                        t = asyncio.create_task(_guest_worker(username, acc["uid"], acc["password"]))
                    else:
                        t = asyncio.create_task(_token_worker(username, acc["token"]))
                    workers[k] = t
                    bot_state.account_workers[username + "::" + k] = t

        # Set status of all other accounts
        for acc in user_accounts:
            k = str(acc.get("uid") if acc.get("type") == "guest" else acc.get("token", "")[:20])
            if not k or k in deleted:
                continue
            if k in paused:
                status_map[k] = "PAUSED"
            elif k in workers and not workers[k].done():
                status_map[k] = "RUNNING"
            elif status_map.get(k) not in ("DONE", "ERROR", "PAUSED", "OFFLINE"):
                status_map[k] = "WAITING"


async def start_user_workers(username):
    await sync_user_queue(username)


async def _guest_worker(username, uid, password):
    try:
        import main as m
    except Exception:
        import app as m
    uid_str = str(uid)
    try:
        while True:
            try:
                if uid_str in USER_DELETED.get(username, set()) or uid_str in USER_PAUSED.get(username, set()):
                    break
                status = USER_STATUS.get(username, {}).get(uid_str, "RUNNING")
                if status != "RUNNING":
                    break

                users = load_users()
                u = users.get(username, {})
                settings = get_user_settings(u)
                max_retries = int(settings.get("login_retry", 3))

                cv = _CURRENT_OWNER.set(username)
                try:
                    print(f"[auth] Guest login starting user={username} uid={uid_str}", flush=True)
                    ad = None
                    try:
                        ad = await m.process_account_uid_pass(uid_str, password)
                    except Exception as ex:
                        print(f"[auth] Login exception for {uid_str}: {ex}", flush=True)

                    if not ad:
                        retries = USER_RETRIES.setdefault(username, {}).get(uid_str, 0) + 1
                        USER_RETRIES[username][uid_str] = retries
                        print(f"[auth] Guest login FAILED user={username} uid={uid_str} ({retries}/{max_retries})", flush=True)
                        if retries >= max_retries:
                            USER_STATUS.setdefault(username, {})[uid_str] = "ERROR"
                            bot_state.log(f"Account {uid_str} failed login {retries} times. Marked ERROR.", "error", uid_str)
                            break
                        await asyncio.sleep(8)
                        continue

                    USER_RETRIES.setdefault(username, {})[uid_str] = 0
                    USER_STATUS.setdefault(username, {})[uid_str] = "RUNNING"
                    acc_id = str(ad.get("account_id", uid_str))

                    if uid_str in USER_DELETED.get(username, set()) or acc_id in USER_DELETED.get(username, set()):
                        break
                    if uid_str in USER_PAUSED.get(username, set()) or acc_id in USER_PAUSED.get(username, set()):
                        break

                    # Propagate mode setting
                    mode_pref = settings.get("game_mode", "AUTO")
                    if mode_pref == "ONLY_BR":
                        bot_state.set_account_mode(acc_id, "BR")
                    elif mode_pref == "ONLY_CS":
                        bot_state.set_account_mode(acc_id, "LW")

                    print(f"[auth] Guest login OK user={username} uid={uid_str} acc_id={acc_id}", flush=True)
                    await m.run_account_worker(ad, uid_str)

                    # Check target completion after match
                    users = load_users()
                    u = users.get(username, {})
                    settings = get_user_settings(u)
                    exp_limit = int(settings.get("exp_limit", 0))
                    level_limit = int(settings.get("level_limit", 0))
                    target_delete = bool(settings.get("target_delete", False))
                    live_acc = ds.bot_state.accounts.get(uid_str) or ds.bot_state.accounts.get(acc_id)
                    cur_gained = live_acc.get("gained_exp", 0) if live_acc else 0
                    cur_level = live_acc.get("level", 1) if live_acc else 1
                    is_done = False
                    if exp_limit > 0 and cur_gained >= exp_limit:
                        is_done = True
                    if level_limit > 0 and cur_level >= level_limit:
                        is_done = True
                    if is_done:
                        USER_STATUS.setdefault(username, {})[uid_str] = "DONE"
                        ds.bot_state.log(f"Account {uid_str} reached target! (Lvl {cur_level}, Gained {cur_gained})", "success", uid_str)
                        if target_delete:
                            USER_DELETED.setdefault(username, set()).add(uid_str)
                            if acc_id:
                                USER_DELETED[username].add(acc_id)
                            u["accounts"] = [a for a in u.get("accounts", []) if str(a.get("uid")) != uid_str]
                            save_users(users)
                            ds.bot_state.accounts.pop(uid_str, None)
                            if acc_id:
                                ds.bot_state.accounts.pop(acc_id, None)
                        break

                    if uid_str in USER_DELETED.get(username, set()) or acc_id in USER_DELETED.get(username, set()):
                        break
                    if uid_str in USER_PAUSED.get(username, set()) or acc_id in USER_PAUSED.get(username, set()):
                        break
                    if USER_STATUS.get(username, {}).get(uid_str) in ("DONE", "ERROR", "WAITING", "PAUSED", "OFFLINE"):
                        break

                    await asyncio.sleep(3)
                finally:
                    try:
                        _CURRENT_OWNER.reset(cv)
                    except Exception:
                        pass
            except asyncio.CancelledError:
                print(f"[auth] Guest worker cancelled user={username} uid={uid_str}", flush=True)
                break
            except Exception as e:
                print(f"[auth] Guest worker error user={username} uid={uid_str}: {e}", flush=True)
                await asyncio.sleep(5)
    finally:
        try:
            workers = USER_WORKERS.get(username)
            if workers is not None:
                if workers.get(uid_str) is asyncio.current_task():
                    workers.pop(uid_str, None)
                loop = asyncio.get_running_loop()
                if loop.is_running():
                    asyncio.create_task(sync_user_queue(username))
        except (RuntimeError, Exception):
            pass


async def _token_worker(username, token):
    try:
        import main as m
    except Exception:
        import app as m
    key = str(token)[:20]
    try:
        while True:
            try:
                if key in USER_DELETED.get(username, set()) or key in USER_PAUSED.get(username, set()):
                    break
                status = USER_STATUS.get(username, {}).get(key, "RUNNING")
                if status != "RUNNING":
                    break

                users = load_users()
                u = users.get(username, {})
                settings = get_user_settings(u)
                max_retries = int(settings.get("login_retry", 3))

                cv = _CURRENT_OWNER.set(username)
                try:
                    print(f"[auth] Token login starting user={username} token={key}...", flush=True)
                    ad = None
                    try:
                        ad = await m.process_account_token(token)
                    except Exception as ex:
                        print(f"[auth] Token login exception for {key}: {ex}", flush=True)

                    if not ad:
                        retries = USER_RETRIES.setdefault(username, {}).get(key, 0) + 1
                        USER_RETRIES[username][key] = retries
                        print(f"[auth] Token login FAILED user={username} token={key} ({retries}/{max_retries})", flush=True)
                        if retries >= max_retries:
                            USER_STATUS.setdefault(username, {})[key] = "ERROR"
                            bot_state.log(f"Token {key} failed login {retries} times. Marked ERROR.", "error", key)
                            break
                        await asyncio.sleep(8)
                        continue

                    USER_RETRIES.setdefault(username, {})[key] = 0
                    USER_STATUS.setdefault(username, {})[key] = "RUNNING"
                    acc_id = str(ad.get("account_id", ""))

                    if key in USER_DELETED.get(username, set()) or acc_id in USER_DELETED.get(username, set()):
                        break
                    if key in USER_PAUSED.get(username, set()) or acc_id in USER_PAUSED.get(username, set()):
                        break

                    mode_pref = settings.get("game_mode", "AUTO")
                    if mode_pref == "ONLY_BR":
                        bot_state.set_account_mode(acc_id, "BR")
                    elif mode_pref == "ONLY_CS":
                        bot_state.set_account_mode(acc_id, "LW")

                    print(f"[auth] Token login OK user={username} acc_id={acc_id}", flush=True)
                    await m.run_account_worker(ad, acc_id)

                    # Check target completion after match
                    users = load_users()
                    u = users.get(username, {})
                    settings = get_user_settings(u)
                    exp_limit = int(settings.get("exp_limit", 0))
                    level_limit = int(settings.get("level_limit", 0))
                    target_delete = bool(settings.get("target_delete", False))
                    live_acc = ds.bot_state.accounts.get(acc_id) or ds.bot_state.accounts.get(key)
                    cur_gained = live_acc.get("gained_exp", 0) if live_acc else 0
                    cur_level = live_acc.get("level", 1) if live_acc else 1
                    is_done = False
                    if exp_limit > 0 and cur_gained >= exp_limit:
                        is_done = True
                    if level_limit > 0 and cur_level >= level_limit:
                        is_done = True
                    if is_done:
                        USER_STATUS.setdefault(username, {})[key] = "DONE"
                        ds.bot_state.log(f"Token {key} reached target! (Lvl {cur_level}, Gained {cur_gained})", "success", key)
                        if target_delete:
                            USER_DELETED.setdefault(username, set()).add(key)
                            if acc_id:
                                USER_DELETED[username].add(acc_id)
                            u["accounts"] = [a for a in u.get("accounts", []) if str(a.get("token", ""))[:20] != key]
                            save_users(users)
                            ds.bot_state.accounts.pop(key, None)
                            if acc_id:
                                ds.bot_state.accounts.pop(acc_id, None)
                        break

                    if key in USER_DELETED.get(username, set()) or acc_id in USER_DELETED.get(username, set()):
                        break
                    if key in USER_PAUSED.get(username, set()) or acc_id in USER_PAUSED.get(username, set()):
                        break
                    if USER_STATUS.get(username, {}).get(key) in ("DONE", "ERROR", "WAITING", "PAUSED", "OFFLINE"):
                        break

                    await asyncio.sleep(3)
                finally:
                    try:
                        _CURRENT_OWNER.reset(cv)
                    except Exception:
                        pass
            except asyncio.CancelledError:
                print(f"[auth] Token worker cancelled user={username}", flush=True)
                break
            except Exception as e:
                print(f"[auth] Token worker error user={username}: {e}", flush=True)
                await asyncio.sleep(5)
    finally:
        try:
            workers = USER_WORKERS.get(username)
            if workers is not None:
                if workers.get(key) is asyncio.current_task():
                    workers.pop(key, None)
                loop = asyncio.get_running_loop()
                if loop.is_running():
                    asyncio.create_task(sync_user_queue(username))
        except (RuntimeError, Exception):
            pass


async def h_root(req):
    s = cur_user(req)
    if not s:
        raise web.HTTPFound("/login")
    un = s.get("username", DEFAULT_USERNAME)
    return web.Response(text=DASHBOARD_HTML.replace("{{USERNAME}}", un), content_type="text/html")


async def h_login_get(req):
    s = cur_user(req)
    if s:
        raise web.HTTPFound("/")
    return web.Response(text=LOGIN_HTML, content_type="text/html")


async def h_login_post(req):
    username = ""
    password = ""
    ct = getattr(req, "content_type", "") or ""
    accept = ""
    if hasattr(req, "headers") and req.headers:
        accept = req.headers.get("Accept", "") or ""

    is_json_req = ("application/json" in ct) or ("application/json" in accept)

    try:
        if "application/json" in ct:
            d = await req.json()
            username = str(d.get("username", "")).strip()
            password = str(d.get("password", "")).strip()
        elif "form" in ct:
            post_data = await req.post()
            username = str(post_data.get("username", "")).strip()
            password = str(post_data.get("password", "")).strip()
        else:
            try:
                d = await req.json()
                username = str(d.get("username", "")).strip()
                password = str(d.get("password", "")).strip()
                is_json_req = True
            except Exception:
                post_data = await req.post()
                username = str(post_data.get("username", "")).strip()
                password = str(post_data.get("password", "")).strip()
    except Exception:
        pass

    valid = False
    u_clean = username.strip()
    u_lower = u_clean.lower()
    p_clean = password.strip()

    if (u_lower == "hh" and p_clean == "hh") or \
       (u_lower == "admin" and p_clean == "admin") or \
       (u_lower == "zahid" and p_clean == "123"):
        valid = True
        username = u_lower
    else:
        users = load_users()
        u = users.get(u_clean) or users.get(u_lower)
        if u:
            ph = u.get("password_hash")
            salt = u.get("salt")
            if ph and salt and verify_pw(p_clean, ph, salt):
                valid = True
                username = u_clean

    if not valid:
        if is_json_req:
            return web.json_response({"status": "error", "error": "Invalid username or password"}, status=401)
        r = web.HTTPFound("/login?error=Invalid+username+or+password")
        raise r

    ensure_user_exists(username)
    token = create_session(username, is_admin=True)
    if is_json_req:
        resp = web.json_response({"status": "ok", "redirect": "/"})
        _set_ck(resp, token)
        return resp

    r = web.HTTPFound("/")
    _set_ck(r, token)
    raise r


async def h_signup(req):
    raise web.HTTPFound("/login")


async def h_plans(req):
    raise web.HTTPFound("/login")


async def h_logout(req):
    token = req.cookies.get(SESSION_COOKIE) if hasattr(req, "cookies") and req.cookies else None
    if token:
        destroy_session(token)
    r = web.HTTPFound("/login")
    _clr_ck(r)
    raise r


async def h_dash(req):
    s = cur_user(req)
    if not s:
        raise web.HTTPFound("/login")
    un = s.get("username", DEFAULT_USERNAME)
    return web.Response(text=DASHBOARD_HTML.replace("{{USERNAME}}", un), content_type="text/html")


async def h_expired(req):
    raise web.HTTPFound("/login")


async def h_stats(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    login_un = s.get("username", "")
    un = get_effective_user(login_un)
    users = load_users()
    if un not in users:
        ensure_user_exists(un)
        users = load_users()
    u = users.get(un, {})
    default_un = ensure_default_user()
    now = time.time()
    expired = False
    left = 999999999
    paused = USER_PAUSED.get(un, set())
    deleted = USER_DELETED.get(un, set())
    status_map = USER_STATUS.setdefault(un, {})
    settings = get_user_settings(u)

    # Periodic lightweight sync of live bot_state → users.json (every ~30s)
    last_sync = _LAST_SYNC.get(un, 0)
    if now - last_sync > 30:
        _LAST_SYNC[un] = now
        asyncio.create_task(sync_user_accounts_to_disk(un))

    user_workers = USER_WORKERS.get(un, {})
    active_worker_count = len([t for t in user_workers.values() if not t.done()])
    active_slots = max(1, int(settings.get("active_slots", 10)))
    total_acc_count = len(u.get("accounts", []))
    if not expired and (un not in USER_WORKERS or (active_worker_count < min(active_slots, total_acc_count) and settings.get("all_bots", True))):
        asyncio.create_task(sync_user_queue(un))

    out = []
    seen_keys = set()

    # Read live bot state
    for uid, a in list(ds.bot_state.accounts.items()):
        if a.get("_owner") != un:
            continue
        if uid in deleted:
            continue
        k_str = str(uid)
        is_paused = k_str in paused
        is_worker_alive = k_str in user_workers and not user_workers[k_str].done()

        # Determine queue status
        if is_paused:
            st = "PAUSED"
        elif status_map.get(k_str) == "DONE":
            st = "DONE"
        elif status_map.get(k_str) == "ERROR":
            st = "ERROR"
        elif is_worker_alive:
            st = "RUNNING"
        elif status_map.get(k_str) == "OFFLINE" or a.get("status") == "OFFLINE":
            st = "OFFLINE"
        else:
            st = status_map.get(k_str, "WAITING")

        status_map[k_str] = st

        # Mode
        card_mode = a.get("mode") or ds.bot_state.get_effective_mode(uid, a.get("level", 1))

        acc_obj = {
            "uid": uid,
            "nickname": a.get("nickname", "?"),
            "region": a.get("region", "IND"),
            "level": a.get("level", 1),
            "initial_exp": a.get("initial_exp", 0),
            "current_exp": a.get("current_exp", 0),
            "gained_exp": a.get("gained_exp", 0),
            "last_gain": a.get("last_gain", 0),
            "last_gain_time": a.get("last_gain_time", 0),
            "matches_played": a.get("matches_played", 0),
            "status": st,
            "mode": card_mode,
            "active_matches": a.get("active_matches", 0),
            "created_at": a.get("created_at"),
            "last_update": a.get("last_update"),
        }
        eta_sec, eta_fmt, pct = compute_account_eta(acc_obj, settings)
        acc_obj["eta_seconds"] = eta_sec
        acc_obj["eta_formatted"] = eta_fmt
        acc_obj["progress_pct"] = pct
        out.append(acc_obj)

        seen_keys.add(k_str)
        try:
            cred = ds.bot_state.account_credentials.get(k_str)
            if cred:
                if cred.get("auth_uid"):
                    seen_keys.add(str(cred.get("auth_uid")))
                if cred.get("auth_token"):
                    seen_keys.add(str(cred.get("auth_token"))[:20])
                if cred.get("account_id"):
                    seen_keys.add(str(cred.get("account_id")))
        except Exception:
            pass

    # Include saved accounts not yet active in bot_state
    for acc in u.get("accounts", []):
        acc_type = acc.get("type")
        key = acc.get("uid") if acc_type == "guest" else acc.get("token", "")[:20]
        if not key:
            continue
        key_str = str(key)
        if key_str in seen_keys or key_str in deleted:
            continue

        is_paused = key_str in paused
        is_worker_alive = key_str in user_workers and not user_workers[key_str].done()

        if is_paused:
            st = "PAUSED"
        elif status_map.get(key_str) == "DONE":
            st = "DONE"
        elif status_map.get(key_str) == "ERROR":
            st = "ERROR"
        elif is_worker_alive:
            st = "RUNNING"
        elif status_map.get(key_str) == "OFFLINE" or acc.get("status") == "OFFLINE":
            st = "OFFLINE"
        else:
            st = status_map.get(key_str, "WAITING")

        status_map[key_str] = st

        saved_exp = acc.get("last_exp", 0)
        saved_level = acc.get("last_level", 1)
        saved_nickname = acc.get("last_nickname", f"User_{key_str[:6]}")
        saved_region = acc.get("last_region", "IND")
        saved_initial = acc.get("initial_exp", saved_exp)
        saved_gained = acc.get("gained_exp", max(0, saved_exp - saved_initial))
        saved_played = acc.get("matches_played", 0)
        saved_created = acc.get("created_at")
        saved_updated = acc.get("last_update")
        saved_mode = acc.get("mode") or ds.bot_state.get_effective_mode(key_str, saved_level)

        acc_obj = {
            "uid": key_str,
            "nickname": saved_nickname,
            "region": saved_region,
            "level": saved_level,
            "initial_exp": saved_initial,
            "current_exp": saved_exp,
            "gained_exp": saved_gained,
            "last_gain": acc.get("last_gain", 0),
            "last_gain_time": acc.get("last_gain_time", 0),
            "matches_played": saved_played,
            "status": st,
            "mode": saved_mode,
            "active_matches": 0,
            "created_at": saved_created,
            "last_update": saved_updated,
        }
        eta_sec, eta_fmt, pct = compute_account_eta(acc_obj, settings)
        acc_obj["eta_seconds"] = eta_sec
        acc_obj["eta_formatted"] = eta_fmt
        acc_obj["progress_pct"] = pct
        out.append(acc_obj)

    # Sort accounts: RUNNING first, then WAITING, then others
    status_order = {"RUNNING": 0, "WAITING": 1, "ONLINE": 2, "DONE": 3, "PAUSED": 4, "ERROR": 5, "OFFLINE": 6}
    out.sort(key=lambda x: (status_order.get(x["status"], 9), -x.get("gained_exp", 0)))

    # Compute Filter counts
    counts = {
        "all": len(out),
        "running": sum(1 for a in out if a["status"] == "RUNNING"),
        "waiting": sum(1 for a in out if a["status"] == "WAITING"),
        "done": sum(1 for a in out if a["status"] == "DONE"),
        "paused": sum(1 for a in out if a["status"] == "PAUSED"),
        "error": sum(1 for a in out if a["status"] == "ERROR"),
        "offline": sum(1 for a in out if a["status"] == "OFFLINE"),
    }

    # Compute Total ETA
    total_sec, total_fmt = compute_total_eta(out, settings)

    # Compute system stats
    ram_used, ram_total, ram_pct, cpu_pct = 256, 512, 50, 15
    try:
        import psutil
        vm = psutil.virtual_memory()
        ram_used = vm.used // (1024 * 1024)
        ram_total = vm.total // (1024 * 1024)
        ram_pct = int(vm.percent)
        cpu_pct = int(psutil.cpu_percent(interval=None))
    except Exception:
        try:
            if os.path.exists("/proc/meminfo"):
                meminfo = {}
                with open("/proc/meminfo", "r") as f:
                    for line in f:
                        parts = line.split(":")
                        if len(parts) == 2:
                            meminfo[parts[0].strip()] = int(parts[1].strip().split()[0])
                total_kb = meminfo.get("MemTotal", 0)
                avail_kb = meminfo.get("MemAvailable", meminfo.get("MemFree", 0))
                used_kb = total_kb - avail_kb
                ram_total = total_kb // 1024
                ram_used = used_kb // 1024
                ram_pct = int((used_kb / total_kb) * 100) if total_kb > 0 else 50
        except Exception:
            pass

    workers_count = sum(len([t for t in w.values() if not t.done()]) for w in USER_WORKERS.values())

    return web.json_response({
        "username": login_un or un,
        "slots": settings.get("active_slots", 10),
        "seconds_left": left,
        "expired": expired,
        "settings": settings,
        "system": {
            "ram_used_mb": ram_used,
            "ram_total_mb": ram_total,
            "ram_pct": ram_pct,
            "cpu_pct": cpu_pct,
            "workers_count": workers_count,
            "ping_ms": 375
        },
        "counts": counts,
        "total_eta_seconds": total_sec,
        "total_eta_formatted": total_fmt,
        "accounts": out,
    })


async def h_settings_save(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    un = get_effective_user(s.get("username", ""))
    users = load_users()
    if un not in users:
        ensure_user_exists(un)
        users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User missing"}, status=404)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})

    new_settings = d.get("settings", {})
    cur_settings = get_user_settings(u)
    cur_settings.update(new_settings)
    u["settings"] = cur_settings
    if "active_slots" in cur_settings:
        u["slots"] = cur_settings["active_slots"]
    users[un] = u
    save_users(users)
    asyncio.create_task(sync_user_queue(un))
    return web.json_response({"status": "ok", "settings": cur_settings})


async def h_acc_bulk_add(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    un = get_effective_user(s.get("username", ""))
    users = load_users()
    if un not in users:
        ensure_user_exists(un)
        users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User missing"}, status=404)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})

    text = str(d.get("text", "")).strip()
    accounts_input = d.get("accounts", [])

    lines = text.splitlines() if text else []
    added = 0
    accs = u.setdefault("accounts", [])
    deleted_set = USER_DELETED.setdefault(un, set())
    paused_set = USER_PAUSED.setdefault(un, set())
    retries_map = USER_RETRIES.setdefault(un, {})
    status_map = USER_STATUS.setdefault(un, {})

    def _unmark_and_reset(k):
        deleted_set.discard(k)
        paused_set.discard(k)
        retries_map[k] = 0
        workers = USER_WORKERS.get(un, {})
        if k not in workers or workers[k].done():
            status_map[k] = "WAITING"
        try:
            ds.cache_invalidate(k)
        except Exception:
            pass

    def _add_or_update_guest(uid, pw):
        nonlocal added
        _unmark_and_reset(uid)
        for a in accs:
            if a.get("type") == "guest" and str(a.get("uid")) == uid:
                a["password"] = pw
                workers = USER_WORKERS.get(un, {})
                if uid not in workers or workers[uid].done():
                    a["status"] = "WAITING"
                added += 1
                return
        accs.append({
            "type": "guest",
            "uid": uid,
            "password": pw,
            "created_at": time.time(),
            "initial_exp": 0,
            "last_exp": 0,
            "gained_exp": 0,
            "last_level": 1,
            "matches_played": 0,
            "status": "WAITING"
        })
        added += 1

    def _add_or_update_token(tk):
        nonlocal added
        prefix = tk[:20]
        _unmark_and_reset(prefix)
        _unmark_and_reset(tk)
        for a in accs:
            if a.get("type") == "token" and str(a.get("token")) == tk:
                workers = USER_WORKERS.get(un, {})
                if prefix not in workers or workers[prefix].done():
                    a["status"] = "WAITING"
                added += 1
                return
        accs.append({
            "type": "token",
            "token": tk,
            "created_at": time.time(),
            "initial_exp": 0,
            "last_exp": 0,
            "gained_exp": 0,
            "last_level": 1,
            "matches_played": 0,
            "status": "WAITING"
        })
        added += 1

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Support separator :, |, or ,
        sep = None
        for s_cand in (":", "|", ","):
            if s_cand in line:
                sep = s_cand
                break
        if sep:
            parts = line.split(sep, 1)
            uid = parts[0].strip()
            pw = parts[1].strip()
            if uid and pw:
                _add_or_update_guest(uid, pw)
        elif len(line) >= 10:
            _add_or_update_token(line)

    for a_in in accounts_input:
        if "uid" in a_in and "password" in a_in:
            uid = str(a_in["uid"]).strip()
            pw = str(a_in["password"]).strip()
            if uid and pw:
                _add_or_update_guest(uid, pw)
        elif "token" in a_in:
            tk = str(a_in["token"]).strip()
            if tk:
                _add_or_update_token(tk)

    u["accounts"] = accs
    users[un] = u
    save_users(users)
    asyncio.create_task(sync_user_queue(un))
    return web.json_response({"status": "ok", "added": added, "total": len(accs)})


async def h_acc_bulk_action(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    un = get_effective_user(s.get("username", ""))
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})

    action = str(d.get("action", "")).lower()
    uids = [str(x).strip() for x in d.get("uids", []) if str(x).strip()]

    users = load_users()
    if un not in users:
        ensure_user_exists(un)
        users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User missing"}, status=404)

    paused = USER_PAUSED.setdefault(un, set())
    deleted = USER_DELETED.setdefault(un, set())
    status_map = USER_STATUS.setdefault(un, {})
    workers = USER_WORKERS.setdefault(un, {})

    if action == "pause":
        for uid in uids:
            paused.add(uid)
            status_map[uid] = "PAUSED"
            t = workers.pop(uid, None)
            if t and not t.done():
                t.cancel()
    elif action in ("resume", "relogin"):
        for uid in uids:
            paused.discard(uid)
            status_map[uid] = "RUNNING"
            USER_RETRIES.setdefault(un, {})[uid] = 0
            try:
                ds.cache_invalidate(uid)
            except Exception:
                pass
            t = workers.pop(uid, None)
            if t and not t.done():
                t.cancel()
    elif action == "move_waiting":
        for uid in uids:
            paused.discard(uid)
            status_map[uid] = "WAITING"
            t = workers.pop(uid, None)
            if t and not t.done():
                t.cancel()
        accs = u.get("accounts", [])
        to_move = [a for a in accs if str(a.get("uid") if a.get("type") == "guest" else a.get("token", "")[:20]) in uids]
        remaining = [a for a in accs if str(a.get("uid") if a.get("type") == "guest" else a.get("token", "")[:20]) not in uids]
        u["accounts"] = remaining + to_move
        save_users(users)
    elif action == "move_running":
        for uid in uids:
            paused.discard(uid)
            status_map[uid] = "RUNNING"
        accs = u.get("accounts", [])
        to_move = [a for a in accs if str(a.get("uid") if a.get("type") == "guest" else a.get("token", "")[:20]) in uids]
        remaining = [a for a in accs if str(a.get("uid") if a.get("type") == "guest" else a.get("token", "")[:20]) not in uids]
        u["accounts"] = to_move + remaining
        save_users(users)
    elif action == "delete":
        for uid in uids:
            deleted.add(uid)
            paused.discard(uid)
            status_map.pop(uid, None)
            t = workers.pop(uid, None)
            if t and not t.done():
                t.cancel()
            try:
                ds.cache_invalidate(uid)
            except Exception:
                pass
            ds.bot_state.accounts.pop(uid, None)
        u["accounts"] = [a for a in u.get("accounts", []) if str(a.get("uid") if a.get("type") == "guest" else a.get("token", "")[:20]) not in deleted]
        save_users(users)

    asyncio.create_task(sync_user_queue(un))
    return web.json_response({"status": "ok", "action": action, "count": len(uids)})


async def h_acc_clear_all(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    un = get_effective_user(s.get("username", ""))
    await stop_user_workers(un)
    users = load_users()
    if un not in users:
        ensure_user_exists(un)
        users = load_users()
    u = users.get(un)
    if u:
        u["accounts"] = []
        save_users(users)
    USER_STATUS.pop(un, None)
    USER_PAUSED.pop(un, None)
    USER_DELETED.pop(un, None)
    USER_RETRIES.pop(un, None)
    for k in list(ds.bot_state.accounts.keys()):
        if ds.bot_state.accounts[k].get("_owner") == un:
            ds.bot_state.accounts.pop(k, None)
    return web.json_response({"status": "ok"})


async def h_acc_check(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    un = get_effective_user(s.get("username", ""))
    users = load_users()
    if un not in users:
        ensure_user_exists(un)
        users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Missing"})
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})

    accs = u.setdefault("accounts", [])
    slots = u.get("slots", 0)
    un_deleted = USER_DELETED.get(un, set())

    try:
        import main as m
    except Exception:
        try:
            import app as m
        except Exception:
            return web.json_response({"status": "error", "error": "Main module unavailable"})

    acc_data = None
    if "uid" in d and "password" in d:
        uid = str(d["uid"]).strip()
        pw = str(d["password"]).strip()
        if not uid or not pw:
            return web.json_response({"status": "error", "error": "UID And Password Required"})
        for a in accs:
            if a.get("type") == "guest" and str(a.get("uid")) == uid:
                return web.json_response({"status": "error", "error": "UID Already Added"})
        cached = m.cache_get(uid)
        if cached and cached.get("level"):
            acc_data = cached
        else:
            try:
                acc_data = await m.process_account_uid_pass(uid, pw)
            except Exception:
                return web.json_response({"status": "error", "error": "Login Failed - Invalid UID/Password"})
    elif "token" in d:
        tk = str(d["token"]).strip()
        if not tk:
            return web.json_response({"status": "error", "error": "Token Required"})
        for a in accs:
            if a.get("type") == "token" and a.get("token") == tk:
                return web.json_response({"status": "error", "error": "Token Already Added"})
        cache_key = f"tok_{tk[:20]}"
        cached = m.cache_get(cache_key)
        if cached and cached.get("level"):
            acc_data = cached
        else:
            try:
                acc_data = await m.process_account_token(tk)
            except Exception:
                return web.json_response({"status": "error", "error": "Login Failed - Invalid Token"})
    else:
        return web.json_response({"status": "error", "error": "Invalid Payload"})

    if not acc_data:
        return web.json_response({"status": "error", "error": "Login Failed"})

    return web.json_response({
        "status": "ok",
        "level": int(acc_data.get("level", 1) or 1),
        "region": str(acc_data.get("region", "") or "").upper(),
        "nickname": str(acc_data.get("nickname", "") or ""),
        "account_id": str(acc_data.get("account_id", "")),
        "mode": ("BR" if int(acc_data.get("level", 1) or 1) <= 2 or int(acc_data.get("level", 1) or 1) >= 40 else "LONE WOLF"),
    })


async def h_acc_add(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    un = get_effective_user(s.get("username", ""))
    users = load_users()
    if un not in users:
        ensure_user_exists(un)
        users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Missing"})
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    accs = u.setdefault("accounts", [])
    slots = u.get("slots", 0)

    un_deleted = USER_DELETED.get(un, set())
    if un not in USER_DELETED:
        USER_DELETED[un] = set()
    if un not in USER_PAUSED:
        USER_PAUSED[un] = set()

    def _clear_all_keys_for(uid_or_token):
        keys = {str(uid_or_token)}
        keys.add(str(uid_or_token)[:20])
        try:
            cred = ds.bot_state.account_credentials.get(str(uid_or_token))
            if cred:
                if cred.get("account_id"):
                    keys.add(str(cred.get("account_id")))
                if cred.get("auth_uid"):
                    keys.add(str(cred.get("auth_uid")))
                if cred.get("auth_token"):
                    keys.add(str(cred.get("auth_token"))[:20])
        except Exception:
            pass
        try:
            for k, cred in list(ds.bot_state.account_credentials.items()):
                if str(cred.get("auth_uid", "")) == str(uid_or_token) or \
                   str(cred.get("account_id", "")) == str(uid_or_token) or \
                   str(cred.get("auth_token", ""))[:20] == str(uid_or_token)[:20]:
                    if cred.get("account_id"):
                        keys.add(str(cred.get("account_id")))
                    if cred.get("auth_uid"):
                        keys.add(str(cred.get("auth_uid")))
                    if cred.get("auth_token"):
                        keys.add(str(cred.get("auth_token"))[:20])
        except Exception:
            pass
        for k in keys:
            USER_DELETED[un].discard(k)
            USER_PAUSED[un].discard(k)
            try:
                ds.cache_invalidate(k)
            except Exception:
                pass
        return keys

    if "uid" in d and "password" in d:
        uid = str(d["uid"]).strip()
        pw = str(d["password"]).strip()
        if not uid or not pw:
            return web.json_response({"status": "error", "error": "UID And Password Required"})
        for a in accs:
            if a.get("type") == "guest" and str(a.get("uid")) == uid:
                return web.json_response({"status": "error", "error": "UID Already Added"})
        cleared = _clear_all_keys_for(uid)
        accs.append({"type": "guest", "uid": uid, "password": pw, "created_at": time.time()})
        print(f"[api] Account add user={un} uid={uid} (guest) cleared={cleared}", flush=True)
    elif "token" in d:
        tk = str(d["token"]).strip()
        if not tk:
            return web.json_response({"status": "error", "error": "Token Required"})
        for a in accs:
            if a.get("type") == "token" and a.get("token") == tk:
                return web.json_response({"status": "error", "error": "Token Already Added"})
        cleared = _clear_all_keys_for(tk)
        accs.append({"type": "token", "token": tk, "created_at": time.time()})
        print(f"[api] Account add user={un} token={tk[:20]}... cleared={cleared}", flush=True)
    else:
        return web.json_response({"status": "error", "error": "Invalid Payload"})

    u["accounts"] = accs
    users[un] = u
    save_users(users)
    asyncio.create_task(start_user_workers(un))
    return web.json_response({"status": "ok"})


async def h_acc_del(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    un = get_effective_user(s.get("username", ""))
    users = load_users()
    if un not in users:
        ensure_user_exists(un)
        users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Missing"})
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    uid = str(d.get("uid", "")).strip()
    if not uid:
        return web.json_response({"status": "error", "error": "Missing UID"})

    print(f"[api] Account delete user={un} uid={uid}", flush=True)

    if un not in USER_DELETED:
        USER_DELETED[un] = set()
    if un not in USER_PAUSED:
        USER_PAUSED[un] = set()

    real_uid = None
    real_token_prefix = None
    try:
        cred = ds.bot_state.account_credentials.get(uid)
        if cred:
            if cred.get("auth_uid"):
                real_uid = str(cred.get("auth_uid"))
            if cred.get("auth_token"):
                real_token_prefix = str(cred.get("auth_token"))[:20]
    except Exception:
        pass

    if real_uid is None and real_token_prefix is None:
        try:
            for k, cred in list(ds.bot_state.account_credentials.items()):
                if str(cred.get("account_id", "")) == uid:
                    if cred.get("auth_uid"):
                        real_uid = str(cred.get("auth_uid"))
                        break
                    if cred.get("auth_token"):
                        real_token_prefix = str(cred.get("auth_token"))[:20]
                        break
        except Exception:
            pass

    USER_DELETED[un].add(uid)
    if real_uid:
        USER_DELETED[un].add(real_uid)
    if real_token_prefix:
        USER_DELETED[un].add(real_token_prefix)
    USER_PAUSED[un].discard(uid)
    if real_uid:
        USER_PAUSED[un].discard(real_uid)
    if real_token_prefix:
        USER_PAUSED[un].discard(real_token_prefix)

    keys_to_kill = [uid]
    if real_uid:
        keys_to_kill.append(real_uid)
    if real_token_prefix:
        keys_to_kill.append(real_token_prefix)

    workers = USER_WORKERS.get(un, {})
    for k in keys_to_kill:
        t = workers.pop(k, None)
        if t and not t.done():
            t.cancel()
            try:
                await asyncio.wait_for(t, timeout=5)
            except (asyncio.CancelledError, asyncio.TimeoutError, Exception):
                pass

    for key in list(bot_state.account_workers.keys()):
        if str(key).startswith(un + "::"):
            suffix = str(key).split("::", 1)[1]
            if suffix in keys_to_kill:
                t = bot_state.account_workers.pop(key, None)
                if t and not t.done():
                    t.cancel()
                    try:
                        await asyncio.wait_for(t, timeout=3)
                    except Exception:
                        pass

    for k in keys_to_kill:
        try:
            ds.cache_invalidate(k)
        except Exception:
            pass

    removed = False
    accs_list = list(u.get("accounts", []))
    for acc in list(accs_list):
        acc_type = acc.get("type")
        acc_uid = str(acc.get("uid", ""))
        acc_token_prefix = str(acc.get("token", ""))[:20]

        match = False
        if acc_type == "guest":
            if acc_uid == uid or (real_uid and acc_uid == real_uid):
                match = True
        elif acc_type == "token":
            if acc_token_prefix == uid[:20] or (real_token_prefix and acc_token_prefix == real_token_prefix):
                match = True

        if match:
            accs_list.remove(acc)
            removed = True
            print(f"[api] Removed from users.json: type={acc_type} uid={acc_uid} token={acc_token_prefix}", flush=True)
            break

    u["accounts"] = accs_list
    users[un] = u
    save_users(users)
    print(f"[api] After delete: {un} now has {len(accs_list)}/{u.get('slots', 0)} slots used", flush=True)

    for k in keys_to_kill:
        if k in bot_state.accounts:
            bot_state.accounts.pop(k, None)

    await asyncio.sleep(0.5)

    for k in keys_to_kill:
        if k in bot_state.accounts:
            bot_state.accounts.pop(k, None)

    asyncio.create_task(sync_user_queue(un))
    return web.json_response({"status": "ok", "removed": removed})


async def h_acc_pause(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    un = get_effective_user(s.get("username", ""))
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    uid = str(d.get("uid", "")).strip()
    if not uid:
        return web.json_response({"status": "error", "error": "Missing UID"})

    print(f"[api] Account pause user={un} uid={uid}", flush=True)

    real_uid = None
    real_token_prefix = None
    try:
        cred = ds.bot_state.account_credentials.get(uid)
        if cred:
            if cred.get("auth_uid"):
                real_uid = str(cred.get("auth_uid"))
            if cred.get("auth_token"):
                real_token_prefix = str(cred.get("auth_token"))[:20]
    except Exception:
        pass

    if un not in USER_PAUSED:
        USER_PAUSED[un] = set()
    USER_PAUSED[un].add(uid)
    if real_uid:
        USER_PAUSED[un].add(real_uid)
    if real_token_prefix:
        USER_PAUSED[un].add(real_token_prefix)

    keys_to_kill = [uid]
    if real_uid:
        keys_to_kill.append(real_uid)
    if real_token_prefix:
        keys_to_kill.append(real_token_prefix)

    workers = USER_WORKERS.get(un, {})
    for k in keys_to_kill:
        t = workers.pop(k, None)
        if t and not t.done():
            t.cancel()
            try:
                await asyncio.wait_for(t, timeout=5)
            except (asyncio.CancelledError, asyncio.TimeoutError, Exception):
                pass

    for key in list(bot_state.account_workers.keys()):
        if str(key).startswith(un + "::"):
            suffix = str(key).split("::", 1)[1]
            if suffix in keys_to_kill:
                t = bot_state.account_workers.pop(key, None)
                if t and not t.done():
                    t.cancel()
                    try:
                        await asyncio.wait_for(t, timeout=3)
                    except Exception:
                        pass

    for k in keys_to_kill:
        if k in bot_state.accounts:
            bot_state.accounts[k]["status"] = "PAUSED"

    asyncio.create_task(sync_user_queue(un))
    return web.json_response({"status": "ok"})


async def h_acc_resume(req):
    s = cur_user(req)
    if not s:
        return web.json_response({"status": "error", "error": "unauthorized", "redirect": "/login"}, status=401)
    un = get_effective_user(s.get("username", ""))
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    uid = str(d.get("uid", "")).strip()
    if not uid:
        return web.json_response({"status": "error", "error": "Missing UID"})

    print(f"[api] Account resume user={un} uid={uid}", flush=True)

    real_uid = None
    real_token_prefix = None
    try:
        cred = ds.bot_state.account_credentials.get(uid)
        if cred:
            if cred.get("auth_uid"):
                real_uid = str(cred.get("auth_uid"))
            if cred.get("auth_token"):
                real_token_prefix = str(cred.get("auth_token"))[:20]
    except Exception:
        pass

    keys_to_release = [uid]
    if real_uid:
        keys_to_release.append(real_uid)
    if real_token_prefix:
        keys_to_release.append(real_token_prefix)

    if un in USER_PAUSED:
        for k in keys_to_release:
            USER_PAUSED[un].discard(k)
    if un in USER_DELETED:
        for k in keys_to_release:
            USER_DELETED[un].discard(k)

    users = load_users()
    u = users.get(un, {})
    default_un = ensure_default_user()
    if un == default_un or time.time() < u.get("expires_at", 0):
        asyncio.create_task(start_user_workers(un))

    return web.json_response({"status": "ok"})


async def h_adm_login_get(req):
    raise web.HTTPFound("/login")


async def h_adm_login_post(req):
    return await h_login_post(req)


async def h_adm_logout(req):
    return await h_logout(req)


async def h_adm_panel(req):
    s = cur_user(req)
    if not s:
        raise web.HTTPFound("/login")
    raise web.HTTPFound("/")


async def h_adm_create(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    u = (d.get("username") or "").strip()
    p = (d.get("password") or "").strip()
    slots = int(d.get("slots", 3))
    hours = int(d.get("hours", 24))
    if not u or not p:
        return web.json_response({"status": "error", "error": "Username And Password Required"})
    if slots < 1 or slots > 20:
        return web.json_response({"status": "error", "error": "Slots Must Be 1-20"})
    if hours < 1 or hours > 8760:
        return web.json_response({"status": "error", "error": "Hours Must Be 1-8760"})
    users = load_users()
    if u in users:
        return web.json_response({"status": "error", "error": "Username Already Exists"})
    ph, salt = hash_pw(p)
    now = time.time()
    users[u] = {
        "password_hash": ph,
        "salt": salt,
        "slots": slots,
        "plan_hours": hours,
        "created_at": now,
        "expires_at": now + hours * 3600,
        "accounts": [],
        "_expired_flag": False,
    }
    save_users(users)
    print(f"[api] Admin created user={u} slots={slots} hours={hours}", flush=True)
    return web.json_response({"status": "ok"})


async def h_adm_list(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    users = load_users()
    out = []
    for un, u in users.items():
        used = sum(1 for a in ds.bot_state.accounts.values() if a.get("_owner") == un)
        out.append({
            "username": un,
            "slots": u.get("slots", 0),
            "used_slots": used,
            "expires_at": u.get("expires_at", 0),
            "created_at": u.get("created_at", 0),
        })
    out.sort(key=lambda x: x.get("created_at", 0), reverse=True)
    return web.json_response({"status": "ok", "users": out})


async def h_adm_ext(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    un = d.get("username", "").strip()
    hours = int(d.get("hours", 24))
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Not Found"})
    now = time.time()
    base = max(now, u.get("expires_at", 0))
    u["expires_at"] = base + hours * 3600
    u["_expired_flag"] = False
    save_users(users)
    if un in USER_DELETED:
        USER_DELETED[un].clear()
    print(f"[api] Admin extended user={un} +{hours}h", flush=True)
    asyncio.create_task(start_user_workers(un))
    return web.json_response({"status": "ok"})


async def h_adm_slot(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    un = d.get("username", "").strip()
    count = int(d.get("count", 1))
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Not Found"})
    u["slots"] = min(20, u.get("slots", 0) + count)
    save_users(users)
    print(f"[api] Admin added {count} slot to user={un}", flush=True)
    return web.json_response({"status": "ok"})


async def h_adm_del(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    un = d.get("username", "").strip()
    users = load_users()
    if un not in users:
        return web.json_response({"status": "error", "error": "User Not Found"})
    print(f"[api] Admin deleted user={un}", flush=True)
    await stop_user_workers(un)
    users.pop(un, None)
    save_users(users)
    USER_PAUSED.pop(un, None)
    USER_DELETED.pop(un, None)
    USER_WORKERS.pop(un, None)
    return web.json_response({"status": "ok"})


async def h_adm_reset_pw(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    un = d.get("username", "").strip()
    new_pw = d.get("password", "").strip()
    if not un or not new_pw:
        return web.json_response({"status": "error", "error": "Username And Password Required"})
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Not Found"})
    ph, salt = hash_pw(new_pw)
    u["password_hash"] = ph
    u["salt"] = salt
    users[un] = u
    save_users(users)
    print(f"[api] Admin reset password user={un}", flush=True)
    return web.json_response({"status": "ok"})


async def expiry_watcher():
    while True:
        await asyncio.sleep(60)


async def queue_watcher():
    """Continuously ensures waiting accounts are promoted to running slots when free."""
    while True:
        try:
            users = load_users()
            now = time.time()
            default_un = ensure_default_user()
            for un, u in users.items():
                if un == default_un or now < u.get("expires_at", 0):
                    await sync_user_queue(un)
        except Exception:
            pass
        await asyncio.sleep(3)


def get_env_port(default: int = 8080) -> int:
    for key in ("PORT", "WEB_PORT"):
        val = str(os.environ.get(key, "")).strip()
        if val.isdigit():
            return int(val)
    return default


async def h_health(req):
    return web.json_response({
        "status": "ok",
        "service": "udp-levelup",
        "timestamp": int(time.time())
    })


async def start_web_dashboard(host=None, port=None):
    if host is None:
        host = os.environ.get("HOST", "0.0.0.0")
    if port is None:
        port = get_env_port(8080)
    else:
        try:
            port = int(port)
        except (ValueError, TypeError):
            port = get_env_port(8080)
    app = web.Application()

    app.router.add_get("/", h_root)
    app.router.add_get("/health", h_health)
    app.router.add_get("/healthz", h_health)
    app.router.add_get("/api/health", h_health)
    app.router.add_get("/login", h_login_get)
    app.router.add_post("/login", h_login_post)
    app.router.add_get("/signup", h_signup)
    app.router.add_post("/signup", h_login_post)
    app.router.add_get("/plans", h_plans)
    app.router.add_post("/plans", h_login_post)
    app.router.add_get("/logout", h_logout)
    app.router.add_post("/logout", h_logout)
    app.router.add_get("/dashboard", h_dash)
    app.router.add_get("/expired", h_expired)
    app.router.add_get("/admin", h_adm_login_get)
    app.router.add_get("/admin/", h_adm_login_get)
    app.router.add_post("/admin", h_adm_login_post)
    app.router.add_post("/admin/", h_adm_login_post)

    app.router.add_get("/api/stats", h_stats)
    app.router.add_post("/api/settings/save", h_settings_save)
    app.router.add_post("/api/account/check", h_acc_check)
    app.router.add_post("/api/account/add", h_acc_add)
    app.router.add_post("/api/account/bulk-add", h_acc_bulk_add)
    app.router.add_post("/api/account/bulk-action", h_acc_bulk_action)
    app.router.add_post("/api/account/clear-all", h_acc_clear_all)
    app.router.add_post("/api/account/delete", h_acc_del)
    app.router.add_post("/api/account/pause", h_acc_pause)
    app.router.add_post("/api/account/resume", h_acc_resume)

    app.router.add_get(ADMIN_PATH, h_adm_login_get)
    app.router.add_post(ADMIN_PATH, h_adm_login_post)
    app.router.add_get(ADMIN_PATH + "/logout", h_adm_logout)
    app.router.add_get(ADMIN_PATH + "/panel", h_adm_panel)

    app.router.add_post("/api/admin/create-user", h_adm_create)
    app.router.add_get("/api/admin/list-users", h_adm_list)
    app.router.add_post("/api/admin/extend-time", h_adm_ext)
    app.router.add_post("/api/admin/add-slot", h_adm_slot)
    app.router.add_post("/api/admin/delete-user", h_adm_del)
    app.router.add_post("/api/admin/reset-password", h_adm_reset_pw)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()

    print(f"Web Dashboard Running On http://{host}:{port}", flush=True)

    asyncio.create_task(expiry_watcher())
    asyncio.create_task(queue_watcher())

    try:
        default_un = ensure_default_user()
        users = load_users()
        now = time.time()
        for un, u in users.items():
            if un == default_un or now < u.get("expires_at", 0):
                asyncio.create_task(start_user_workers(un))
    except Exception as e:
        print(f"[auth] Startup user initialization error: {e}", flush=True)


__all__ = ["bot_state", "start_web_dashboard"]