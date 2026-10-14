# -*- coding: utf-8 -*-

_FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Orbitron:wght@500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Inter',system-ui,sans-serif;background:#000;color:#fff;min-height:100vh;-webkit-font-smoothing:antialiased}
:root{--bg:#000;--card:#08080c;--card2:#101015;--line:#1a1a22;--line2:#25252e;--txt:#fff;--mut:#8a8a95;--dim:#55555f;--green:#22c55e;--red:#ef4444;--blue:#3b82f6;--purple:#8b5cf6;--gold:#f59e0b}
.mono{font-family:'JetBrains Mono',monospace}
.orb{font-family:'Orbitron',sans-serif}
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-track{background:#0a0a0a}
::-webkit-scrollbar-thumb{background:#262626;border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:#3a3a3a}
"""

_ICONS = {
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "fast": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 19 22 12 13 5 13 19"></polygon><polygon points="2 19 11 12 2 5 2 19"></polygon></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
    "refresh": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>',
    "cloud": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "list": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="6" height="4" rx="1"></rect><rect x="3" y="15" width="6" height="4" rx="1"></rect><line x1="14" y1="7" x2="21" y2="7"></line><line x1="14" y1="17" x2="21" y2="17"></line></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    "crown": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-1.5-9-4 3-4.5-7-4.5 7-4-3z"></path></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>',
    "pause": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="4" width="4" height="16" rx="1"></rect><rect x="14" y="4" width="4" height="16" rx="1"></rect></svg>',
    "play": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="6 4 20 12 6 20 6 4"></polygon></svg>',
    "trash": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"></path><path d="M10 11v6M14 11v6"></path><path d="M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"></path></svg>',
    "monitor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',
    "gamepad": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"></line><line x1="8" y1="10" x2="8" y2="14"></line><line x1="15" y1="13" x2="15.01" y2="13"></line><line x1="18" y1="11" x2="18.01" y2="11"></line><rect x="2" y="6" width="20" height="12" rx="6"></rect></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
    "id": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"></rect><circle cx="9" cy="11" r="2"></circle><path d="M15 10h3M15 14h3"></path></svg>',
    "trophy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M12 17v4M7 4h10v6a5 5 0 0 1-10 0V4z"></path><path d="M17 5h3a2 2 0 0 1 0 4h-1M7 5H4a2 2 0 0 0 0 4h1"></path></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>',
    "warn": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
    "plus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>',
    "arrow_right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    "star_fill": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    "bolt_fill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "crown_fill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-1.5-9-4 3-4.5-7-4.5 7-4-3z"></path></svg>',
}


def _icon(name, color="currentColor", size=16, stroke_extra=""):
    svg = _ICONS.get(name, "")
    if not svg:
        return ""
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"')
    svg = svg.replace('<svg ', f'<svg width="{size}" height="{size}" ', 1)
    return svg


def _icon_inline(name, color="currentColor", size=16):
    svg = _ICONS.get(name, "")
    if not svg:
        return ""
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"')
    svg = svg.replace('<svg ', f'<svg width="{size}" height="{size}" style="display:inline-block;vertical-align:middle" ', 1)
    return svg


# ==================== DASHBOARD ====================
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Dashboard - hh X LevelUp</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:radial-gradient(ellipse at top,#080e1a 0%,#000 60%);padding-bottom:80px;overflow-x:hidden}
*{-webkit-tap-highlight-color:transparent}

/* ===== TOP BAR ===== */
.top{position:sticky;top:0;z-index:50;background:rgba(4,7,15,0.92);backdrop-filter:blur(16px);border-bottom:1px solid rgba(59,130,246,0.18)}
.top-in{max-width:1380px;margin:0 auto;padding:10px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.logo{display:flex;align-items:center;gap:8px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;letter-spacing:1.5px}
.lm{width:28px;height:28px;background:linear-gradient(135deg,#3b82f6,#8b5cf6);color:#fff;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:13px;box-shadow:0 0 12px rgba(59,130,246,0.4)}

/* Header System Stats */
.header-stats{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.h-stat-pill{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:8px;
  padding:5px 10px;
  font-family:'JetBrains Mono',monospace;
  font-size:11px;
  font-weight:600;
  color:#cbd5e1;
}
.h-stat-pill .lbl{font-family:'Orbitron',sans-serif;font-size:8px;font-weight:800;color:var(--mut);letter-spacing:1px;text-transform:uppercase}
.h-stat-pill.ping .val{color:#22c55e}
.h-stat-pill.ram .val{color:#60a5fa}
.h-stat-pill.cpu .val{color:#f59e0b}
.h-stat-pill.workers .val{color:#c084fc}

.btn-clear-all{
  background:rgba(239,68,68,0.12);
  border:1px solid rgba(239,68,68,0.45);
  color:#ef4444;
  border-radius:8px;
  padding:6px 12px;
  font-family:'Orbitron',sans-serif;
  font-size:10px;
  font-weight:700;
  letter-spacing:1.2px;
  cursor:pointer;
  transition:all 0.2s;
  text-transform:uppercase;
  display:inline-flex;
  align-items:center;
  gap:5px;
}
.btn-clear-all:hover{background:rgba(239,68,68,0.22);border-color:#ef4444;box-shadow:0 0 12px rgba(239,68,68,0.3)}

.user-meta{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.mi{display:flex;flex-direction:column;gap:1px;padding:3px 8px;border-left:2px solid #3b82f6}
.mi .l{font-size:8px;color:var(--mut);letter-spacing:1px;text-transform:uppercase;font-weight:800;font-family:'Orbitron',sans-serif}
.mi .v{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;white-space:nowrap}
.act{display:flex;gap:6px}
.bs{padding:7px 11px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;border-radius:7px;cursor:pointer;text-decoration:none;border:1px solid transparent;display:inline-flex;align-items:center;justify-content:center;gap:4px;transition:all 0.2s;white-space:nowrap}
.bw{background:#fff;color:#000}
.bw:hover{opacity:0.88}
.bg{background:transparent;border-color:var(--line2);color:var(--mut)}
.bg:hover{border-color:var(--red);color:var(--red)}
.bf{background:transparent;border-color:var(--line2);color:#fff;width:32px;height:32px;padding:0}
.bf:hover{background:var(--card2)}
.bf.sp svg{animation:sp 0.7s linear infinite}
@keyframes sp{to{transform:rotate(360deg)}}
@keyframes pl{0%,100%{opacity:1}50%{opacity:0.35}}

/* ===== MAIN CONTAINER ===== */
.main{max-width:1380px;margin:0 auto;padding:16px 14px 60px}

/* ===== CONTROL PANELS GRID ===== */
.panels-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}
@media(max-width:860px){.panels-grid{grid-template-columns:1fr}}

.panel-card{
  background:linear-gradient(145deg,#0d1424 0%,#080c16 100%);
  border:1px solid #1a2842;
  border-radius:14px;
  padding:16px 18px;
  box-shadow:0 8px 24px rgba(0,0,0,0.4);
}
.panel-head{
  display:flex;align-items:center;justify-content:space-between;
  margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,0.06);
}
.panel-head h2{
  font-family:'Orbitron',sans-serif;font-size:12px;font-weight:800;letter-spacing:1.5px;
  color:#93c5fd;text-transform:uppercase;margin:0;display:flex;align-items:center;gap:6px;
}
.panel-body{display:flex;flex-direction:column;gap:12px}

.ctrl-row{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
.ctrl-row label{font-size:11px;font-weight:700;color:#94a3b8;font-family:'Inter',sans-serif;letter-spacing:0.4px}

.toggle-btn{
  background:rgba(255,255,255,0.05);
  border:1px solid rgba(255,255,255,0.14);
  color:#cbd5e1;
  padding:8px 14px;
  border-radius:8px;
  font-family:'Orbitron',sans-serif;
  font-size:10px;
  font-weight:700;
  letter-spacing:1px;
  cursor:pointer;
  transition:all 0.2s;
  display:inline-flex;
  align-items:center;
  gap:6px;
}
.toggle-btn.on{
  background:rgba(34,197,94,0.15);
  border-color:rgba(34,197,94,0.5);
  color:#22c55e;
  box-shadow:0 0 10px rgba(34,197,94,0.15);
}
.toggle-btn.off{
  background:rgba(239,68,68,0.12);
  border-color:rgba(239,68,68,0.45);
  color:#ef4444;
}

/* Stepper */
.stepper{display:inline-flex;align-items:center;background:#101726;border:1px solid #1e293b;border-radius:8px;overflow:hidden}
.step-btn{
  background:transparent;border:none;color:#fff;
  width:32px;height:32px;font-size:16px;font-weight:700;cursor:pointer;
  display:flex;align-items:center;justify-content:center;transition:background 0.15s;
}
.step-btn:hover{background:rgba(59,130,246,0.2)}
.stepper input{
  width:48px;background:transparent;border:none;color:#fff;
  font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:700;
  text-align:center;outline:none;-moz-appearance:textfield;
}
.stepper input::-webkit-outer-spin-button,.stepper input::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}

.num-inp{
  background:#101726;border:1px solid #1e293b;border-radius:8px;
  padding:6px 10px;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;
  font-weight:700;width:90px;text-align:right;outline:none;
}
.num-inp:focus{border-color:#3b82f6}

.input-btn-group{display:inline-flex;align-items:center;gap:6px}
.btn-set{
  background:linear-gradient(135deg,#3b82f6,#2563eb);
  border:none;color:#fff;border-radius:7px;padding:7px 12px;
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;cursor:pointer;letter-spacing:1px;
}
.btn-set:hover{opacity:0.9}

.sub-desc{font-size:10px;color:#64748b;font-family:'Inter',sans-serif;margin-top:2px}

/* Mode selector */
.mode-selector{display:inline-flex;gap:4px;background:#0c121e;padding:3px;border-radius:8px;border:1px solid #1e293b}
.mode-btn{
  background:transparent;border:none;color:var(--mut);
  padding:6px 10px;border-radius:6px;font-family:'Orbitron',sans-serif;font-size:9px;
  font-weight:700;cursor:pointer;letter-spacing:1px;transition:all 0.2s;
}
.mode-btn.on{background:#3b82f6;color:#fff;box-shadow:0 0 10px rgba(59,130,246,0.4)}

.btn-save-settings{
  width:100%;background:linear-gradient(135deg,#3b82f6,#1d4ed8);
  border:none;color:#fff;border-radius:8px;padding:10px;
  font-family:'Orbitron',sans-serif;font-size:10px;font-weight:800;letter-spacing:1.5px;
  cursor:pointer;text-transform:uppercase;transition:all 0.2s;margin-top:4px;
}
.btn-save-settings:hover{box-shadow:0 0 16px rgba(59,130,246,0.45)}

/* Total ETA Banner */
.total-eta-box{
  background:rgba(59,130,246,0.08);border:1px solid rgba(59,130,246,0.25);
  border-radius:9px;padding:9px 12px;display:flex;align-items:center;justify-content:space-between;
  margin-top:4px;
}
.total-eta-box .lbl{font-family:'Orbitron',sans-serif;font-size:10px;font-weight:800;color:#93c5fd;letter-spacing:1px}
.total-eta-box .val{font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:800;color:#22c55e}

/* ===== FILTER TABS & BULK TOOLBAR ===== */
.filter-bar{
  background:linear-gradient(145deg,#0d1424 0%,#080c16 100%);
  border:1px solid #1a2842;border-radius:14px;padding:12px 14px;
  margin-bottom:14px;display:flex;flex-direction:column;gap:12px;
}
.filter-tabs{display:flex;gap:6px;overflow-x:auto;padding-bottom:2px}
.f-tab{
  background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
  border-radius:8px;padding:7px 12px;color:#94a3b8;font-family:'Orbitron',sans-serif;
  font-size:10px;font-weight:700;letter-spacing:0.8px;cursor:pointer;
  white-space:nowrap;display:inline-flex;align-items:center;gap:6px;transition:all 0.18s;
}
.f-tab:hover{background:rgba(255,255,255,0.08);color:#fff}
.f-tab.active{background:rgba(59,130,246,0.18);border-color:#3b82f6;color:#fff;box-shadow:0 0 10px rgba(59,130,246,0.2)}
.f-tab .cnt{
  background:rgba(0,0,0,0.4);border-radius:10px;padding:1px 6px;
  font-family:'JetBrains Mono',monospace;font-size:9px;font-weight:800;color:#cbd5e1;
}

.bulk-toolbar{
  display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;
  padding-top:10px;border-top:1px solid rgba(255,255,255,0.06);
}
.bulk-left{display:flex;align-items:center;gap:12px}
.chk-mark-all{display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:700;color:#cbd5e1;cursor:pointer;font-family:'Inter',sans-serif}
.chk-mark-all input{cursor:pointer;width:15px;height:15px;accent-color:#3b82f6}
.sel-count{font-family:'JetBrains Mono',monospace;font-size:11px;color:#60a5fa;font-weight:700}

.bulk-actions{display:flex;gap:6px;flex-wrap:wrap}
.b-act-btn{
  background:#141d2e;border:1px solid #1f2e48;border-radius:7px;
  padding:6px 11px;color:#cbd5e1;font-family:'Inter',sans-serif;font-size:11px;
  font-weight:700;cursor:pointer;display:inline-flex;align-items:center;gap:5px;
  transition:all 0.18s;
}
.b-act-btn:hover{background:#1e2c45;border-color:#3b82f6;color:#fff}
.b-act-btn.del{border-color:rgba(239,68,68,0.4);color:#ef4444}
.b-act-btn.del:hover{background:rgba(239,68,68,0.18);border-color:#ef4444}

.btn-add-accs{
  background:linear-gradient(135deg,#22c55e,#16a34a);
  border:none;color:#fff;border-radius:8px;padding:7px 14px;
  font-family:'Orbitron',sans-serif;font-size:10px;font-weight:800;letter-spacing:1px;
  cursor:pointer;display:inline-flex;align-items:center;gap:6px;transition:all 0.2s;
}
.btn-add-accs:hover{box-shadow:0 0 14px rgba(34,197,94,0.4)}

/* ===== SMALL CARD SYSTEM ===== */
.cards-grid{
  display:grid;
  grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));
  gap:12px;
}
.acc-card{
  background:linear-gradient(145deg,#0c1322 0%,#080c16 100%);
  border:1px solid #192740;
  border-radius:12px;
  padding:12px;
  position:relative;
  transition:border-color 0.2s, box-shadow 0.2s, transform 0.15s;
  display:flex;flex-direction:column;gap:10px;
}
.acc-card:hover{
  border-color:#253c63;
  box-shadow:0 4px 20px rgba(0,0,0,0.5), 0 0 10px rgba(59,130,246,0.1);
}
.acc-card.selected{
  border-color:#3b82f6;
  box-shadow:0 0 0 1px #3b82f6, 0 4px 20px rgba(59,130,246,0.25);
}

.card-top{display:flex;align-items:center;justify-content:space-between;gap:6px}
.card-top-left{display:flex;align-items:center;gap:6px}
.card-chk{width:15px;height:15px;cursor:pointer;accent-color:#3b82f6}

.status-pill{
  display:inline-flex;align-items:center;gap:5px;
  border-radius:14px;padding:3px 8px;font-family:'Orbitron',sans-serif;
  font-size:8px;font-weight:800;letter-spacing:1px;text-transform:uppercase;
}
.status-pill .dot{width:5px;height:5px;border-radius:50%}

.status-running{background:rgba(34,197,94,0.12);border:1px solid rgba(34,197,94,0.4);color:#22c55e}
.status-running .dot{background:#22c55e;box-shadow:0 0 6px #22c55e;animation:pl 1.4s infinite}

.status-waiting{background:rgba(245,158,11,0.12);border:1px solid rgba(245,158,11,0.4);color:#f59e0b}
.status-waiting .dot{background:#f59e0b;box-shadow:0 0 4px #f59e0b}

.status-done{background:rgba(16,185,129,0.14);border:1px solid rgba(16,185,129,0.5);color:#10b981}
.status-done .dot{background:#10b981;box-shadow:0 0 6px #10b981}

.status-paused{background:rgba(148,163,184,0.1);border:1px solid rgba(148,163,184,0.3);color:#94a3b8}
.status-paused .dot{background:#94a3b8}

.status-error{background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.4);color:#ef4444}
.status-error .dot{background:#ef4444;box-shadow:0 0 6px #ef4444}

.status-offline{background:rgba(100,116,139,0.1);border:1px solid rgba(100,116,139,0.25);color:#64748b}
.status-offline .dot{background:#64748b}

.tag-pill{
  background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
  border-radius:6px;padding:2px 7px;font-family:'Orbitron',sans-serif;font-size:8px;
  font-weight:700;color:#94a3b8;letter-spacing:0.8px;
}
.tag-pill.tag-mode{border-color:rgba(168,85,247,0.35);color:#c084fc}

/* Profile row */
.card-profile{display:flex;align-items:center;gap:10px}
.avatar-small{
  width:36px;height:36px;border-radius:9px;
  background:linear-gradient(135deg,#1e314f,#101e33);
  border:1px solid rgba(59,130,246,0.3);
  display:flex;align-items:center;justify-content:center;
  font-family:'Orbitron',sans-serif;font-weight:900;font-size:14px;color:#fff;
  flex-shrink:0;
}
.prof-info{flex:1;min-width:0}
.prof-name-row{display:flex;align-items:center;justify-content:space-between;gap:4px}
.prof-name{
  font-family:'Orbitron',sans-serif;font-size:12px;font-weight:800;color:#fff;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}
.lvl-badge{
  background:linear-gradient(135deg,#3b82f6,#8b5cf6);
  border-radius:5px;padding:2px 6px;font-family:'Orbitron',sans-serif;
  font-size:9px;font-weight:800;color:#fff;letter-spacing:0.8px;white-space:nowrap;
}
.prof-uid{
  font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--mut);
  margin-top:2px;letter-spacing:0.3px;
}

/* Target & ETA */
.card-target-box{
  background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.05);
  border-radius:7px;padding:6px 8px;
}
.target-labels{display:flex;justify-content:space-between;align-items:center;font-size:9px;font-family:'Orbitron',sans-serif;margin-bottom:4px}
.target-labels .lbl{color:var(--mut)}
.target-labels .eta{color:#22c55e;font-weight:800;font-family:'JetBrains Mono',monospace}
.prog-bar{width:100%;height:4px;background:#141e30;border-radius:2px;overflow:hidden}
.prog-fill{height:100%;background:linear-gradient(90deg,#3b82f6,#22c55e);transition:width 0.4s}

/* Stats 3-box */
.card-stats{display:grid;grid-template-columns:1fr 1fr 1fr;background:rgba(0,0,0,0.3);border-radius:8px;border:1px solid rgba(255,255,255,0.05);overflow:hidden}
.c-stat{padding:7px 4px;text-align:center;border-right:1px solid rgba(255,255,255,0.05)}
.c-stat:last-child{border-right:none}
.c-stat .l{font-size:7px;color:var(--mut);font-family:'Orbitron',sans-serif;font-weight:800;letter-spacing:1px;text-transform:uppercase;margin-bottom:2px}
.c-stat .v{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:800;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.c-stat .v.g{color:#22c55e;white-space:normal;overflow:visible;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:2px}

/* Green + Number gain badge */
.gain-pop-green{
  display:inline-flex;
  align-items:center;
  color:#22c55e;
  background:rgba(34,197,94,0.18);
  border:1px solid rgba(34,197,94,0.5);
  padding:1px 5px;
  border-radius:5px;
  font-size:9px;
  font-weight:800;
  animation:popGreen 1.2s infinite alternate;
}
@keyframes popGreen{
  0%{transform:scale(1);box-shadow:0 0 3px rgba(34,197,94,0.3)}
  100%{transform:scale(1.08);box-shadow:0 0 8px rgba(34,197,94,0.7)}
}

/* Card Action icons */
.card-actions{display:flex;gap:5px;margin-top:auto}
.c-btn{
  flex:1;padding:7px 4px;background:#131c2b;border:1px solid #1e2c45;
  border-radius:6px;color:#cbd5e1;font-family:'Inter',sans-serif;font-size:10px;
  font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;
  gap:3px;transition:all 0.18s;
}
.c-btn:hover{background:#1b283e;border-color:#3b82f6;color:#fff}
.c-btn.del{border-color:rgba(239,68,68,0.35);color:#ef4444}
.c-btn.del:hover{background:rgba(239,68,68,0.18);border-color:#ef4444}

/* Empty State */
.empty-box{grid-column:1/-1;text-align:center;padding:50px 20px;color:var(--mut)}
.empty-box .big{margin-bottom:12px;opacity:0.3}

/* MODALS */
.modal{position:fixed;inset:0;background:rgba(0,0,0,0.9);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:100;padding:16px}
.modal.on{display:flex}
.mc{background:#0c121e;border:1px solid #1e2c45;border-radius:16px;padding:20px;max-width:540px;width:100%;max-height:90vh;overflow-y:auto;box-shadow:0 12px 40px rgba(0,0,0,0.8)}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px}
.mh h3{font-family:'Orbitron',sans-serif;font-size:13px;font-weight:800;letter-spacing:1.5px;color:#93c5fd;text-transform:uppercase}
.mx{background:transparent;border:none;color:var(--mut);cursor:pointer;padding:0;width:28px;height:28px;display:flex;align-items:center;justify-content:center;border-radius:6px;font-size:16px}
.mx:hover{background:#1e293b;color:#fff}

.f{margin-bottom:12px}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.2px;margin-bottom:6px}
.f textarea,.f input{width:100%;background:#080d16;border:1px solid #1a2842;border-radius:8px;padding:10px 12px;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;outline:none;resize:vertical}
.f textarea:focus,.f input:focus{border-color:#3b82f6;box-shadow:0 0 0 2px rgba(59,130,246,0.15)}

.sb{width:100%;padding:12px;border-radius:8px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;border:none;background:linear-gradient(135deg,#3b82f6,#2563eb);color:#fff;transition:all 0.2s}
.sb:hover{box-shadow:0 6px 20px rgba(59,130,246,0.45)}
.sb:disabled{opacity:0.5;cursor:not-allowed}

.err{background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.4);color:var(--red);padding:10px;border-radius:8px;font-size:12px;margin-bottom:12px;display:none}
.err.on{display:block}

/* Confirm modal */
.conf{position:fixed;inset:0;background:rgba(0,0,0,0.88);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:200;padding:18px}
.conf.on{display:flex}
.conf-box{background:#0e1524;border:1px solid #20314f;border-radius:14px;padding:22px;max-width:400px;width:100%;font-family:'Inter',sans-serif;box-shadow:0 10px 35px rgba(0,0,0,0.8)}
.conf-head{font-size:16px;font-weight:800;color:#fff;margin-bottom:10px;text-align:center;font-family:'Orbitron',sans-serif;letter-spacing:1px}
.conf-msg{font-size:13px;line-height:1.6;color:#94a3b8;text-align:center;margin-bottom:20px}
.conf-btns{display:flex;gap:10px}
.conf-btns button{flex:1;padding:11px 10px;border-radius:8px;font-family:'Inter',sans-serif;font-size:12px;font-weight:800;cursor:pointer;border:none;transition:all 0.2s}
.conf-yes{background:#ef4444;color:#fff}
.conf-yes:hover{background:#dc2626}
.conf-no{background:#1e293b;color:#fff}
.conf-no:hover{background:#334155}
</style>
</head>
<body>

<!-- TOP HEADER -->
<div class="top">
  <div class="top-in">
    <div class="logo">
      <span class="lm">M</span>
      <span>hh X LEVELUP</span>
    </div>

    <!-- Live System Stats from requirements -->
    <div class="header-stats">
      <div class="h-stat-pill ping" title="Ping latency">
        <span class="lbl">⚡</span>
        <span class="val" id="hdr-ping">375ms</span>
      </div>
      <div class="h-stat-pill ram" title="System RAM">
        <span class="lbl">RAM</span>
        <span class="val" id="hdr-ram">209908/330437MB (63%)</span>
      </div>
      <div class="h-stat-pill cpu" title="System CPU">
        <span class="lbl">CPU</span>
        <span class="val" id="hdr-cpu">17%</span>
      </div>
      <div class="h-stat-pill workers" title="Active Workers">
        <span class="lbl">Workers</span>
        <span class="val" id="hdr-workers">9</span>
      </div>
      <button class="btn-clear-all" onclick="confirmClearAll()">Clear All IDs</button>
    </div>

    <!-- User Meta & Logout -->
    <div class="user-meta">
      <div class="mi"><span class="l">User</span><span class="v" id="ui-u">{{USERNAME}}</span></div>
      <div class="mi"><span class="l">Status</span><span class="v" id="ui-t" style="color:#22c55e">ONLINE</span></div>
      <div class="act">
        <button class="bs bf" id="rf" title="Refresh">__ICON_REFRESH__</button>
        <a href="/logout" class="bs bg" style="color:#ef4444;border-color:rgba(239,68,68,0.4)" title="Logout">LOGOUT</a>
      </div>
    </div>
  </div>
</div>

<!-- MAIN WORKSPACE -->
<div class="main">

  <!-- PANELS: Queue & limits + CONTROLS -->
  <div class="panels-grid">
    
    <!-- PANEL A: Queue & limits -->
    <div class="panel-card">
      <div class="panel-head">
        <h2>Queue &amp; limits</h2>
      </div>
      <div class="panel-body">
        
        <div class="ctrl-row">
          <label>DAILY AUTO-PLAY:</label>
          <button type="button" id="btn-daily-autoplay" class="toggle-btn off" onclick="toggleDailyAutoplay()">DAILY AUTO-PLAY: <span id="val-daily-autoplay">OFF</span></button>
        </div>

        <div class="ctrl-row">
          <label>Days:</label>
          <input type="number" id="inp-days" class="num-inp" value="1" min="1">
        </div>

        <div class="ctrl-row">
          <label>Active slots</label>
          <div class="stepper">
            <button type="button" class="step-btn" onclick="adjustSlots(-1)">−</button>
            <input type="number" id="inp-slots" value="10" min="1">
            <button type="button" class="step-btn" onclick="adjustSlots(1)">+</button>
          </div>
        </div>

        <div class="ctrl-row">
          <label>Login Retry</label>
          <input type="number" id="inp-retry" class="num-inp" value="3" min="1">
        </div>

        <div class="ctrl-row">
          <label>Daily limit</label>
          <input type="number" id="inp-daily-limit" class="num-inp" value="60000" min="0">
        </div>

        <button type="button" class="btn-save-settings" onclick="saveSettings()">Save Settings</button>
      </div>
    </div>

    <!-- PANEL B: CONTROLS -->
    <div class="panel-card">
      <div class="panel-head">
        <h2>CONTROLS</h2>
      </div>
      <div class="panel-body">
        
        <div class="ctrl-row">
          <label>All Bots on/off</label>
          <button type="button" id="btn-all-bots" class="toggle-btn on" onclick="toggleAllBots()">All Bots: <span id="val-all-bots">ON</span></button>
        </div>

        <div class="ctrl-row">
          <label>Target complete delete on/off</label>
          <button type="button" id="btn-target-delete" class="toggle-btn off" onclick="toggleTargetDelete()">Target complete delete: <span id="val-target-delete">OFF</span></button>
        </div>

        <div>
          <div class="ctrl-row">
            <label>EXP limit (target complete)</label>
            <div class="input-btn-group">
              <input type="number" id="inp-exp-limit" class="num-inp" value="0" min="0">
              <button type="button" class="btn-set" onclick="setExpLimit()">Set</button>
            </div>
          </div>
          <div class="sub-desc" id="hint-exp-limit">No limit (accounts are never auto-deleted)</div>
        </div>

        <div>
          <div class="ctrl-row">
            <label>Level limit (target complete)</label>
            <div class="input-btn-group">
              <input type="number" id="inp-level-limit" class="num-inp" value="21" min="1">
              <button type="button" class="btn-set" onclick="setLevelLimit()">Set</button>
            </div>
          </div>
          <div class="sub-desc" id="hint-level-limit">Target: Level 21</div>
        </div>

        <div class="ctrl-row">
          <label>Game Mode</label>
          <div class="mode-selector">
            <button type="button" class="mode-btn on" id="mode-btn-auto" onclick="setGameMode('AUTO')">AUTO MODE</button>
            <button type="button" class="mode-btn" id="mode-btn-br" onclick="setGameMode('ONLY_BR')">ONLY BR</button>
            <button type="button" class="mode-btn" id="mode-btn-cs" onclick="setGameMode('ONLY_CS')">ONLY CS</button>
          </div>
        </div>

        <div class="total-eta-box">
          <span class="lbl">TOTAL ETA:</span>
          <span class="val" id="val-total-eta">--</span>
        </div>

      </div>
    </div>

  </div>

  <!-- FILTER & BULK TOOLBAR -->
  <div class="filter-bar">
    <div class="filter-tabs">
      <button type="button" class="f-tab active" data-filter="all" onclick="setFilter('all')">All <span class="cnt" id="cnt-all">0</span></button>
      <button type="button" class="f-tab" data-filter="running" onclick="setFilter('running')">Running <span class="cnt" id="cnt-running">0</span></button>
      <button type="button" class="f-tab" data-filter="waiting" onclick="setFilter('waiting')">Waiting <span class="cnt" id="cnt-waiting">0</span></button>
      <button type="button" class="f-tab" data-filter="done" onclick="setFilter('done')">Done <span class="cnt" id="cnt-done">0</span></button>
      <button type="button" class="f-tab" data-filter="paused" onclick="setFilter('paused')">Paused <span class="cnt" id="cnt-paused">0</span></button>
      <button type="button" class="f-tab" data-filter="error" onclick="setFilter('error')">Error <span class="cnt" id="cnt-error">0</span></button>
      <button type="button" class="f-tab" data-filter="offline" onclick="setFilter('offline')">Offline <span class="cnt" id="cnt-offline">0</span></button>
    </div>

    <div class="bulk-toolbar">
      <div class="bulk-left">
        <label class="chk-mark-all">
          <input type="checkbox" id="chk-all" onchange="toggleSelectAll(this.checked)"> Mark All
        </label>
        <span class="sel-count">Selected: <span id="sel-count-num">0</span></span>
      </div>

      <div class="bulk-actions">
        <button type="button" class="b-act-btn" onclick="bulkAction('pause')">⏸ Pause</button>
        <button type="button" class="b-act-btn" onclick="bulkAction('relogin')">🔄 Relogin</button>
        <button type="button" class="b-act-btn" onclick="bulkAction('move_waiting')">⏳ Move to Waiting</button>
        <button type="button" class="b-act-btn" onclick="bulkAction('move_running')">▶ Move to Running</button>
        <button type="button" class="b-act-btn del" onclick="bulkAction('delete')">🗑 Delete</button>
        <button type="button" class="btn-add-accs" onclick="openBulkAdd()">+ Add Accounts</button>
      </div>
    </div>
  </div>

  <!-- SMALL CARD SYSTEM GRID -->
  <div class="cards-grid" id="grid"></div>

</div>

<!-- UNLIMITED BULK ADD MODAL -->
<div class="modal" id="modal-bulk-add">
  <div class="mc">
    <div class="mh">
      <h3>Add Free Fire Accounts (Unlimited)</h3>
      <button class="mx" onclick="closeBulkAdd()">✕</button>
    </div>
    <div class="err" id="bulk-err"></div>
    <p style="font-size:11px;color:#94a3b8;margin-bottom:10px;line-height:1.5">
      Paste unlimited accounts in <code>uid:password</code> format, one per line (or Access Tokens). Extra accounts will safely queue in Waiting and only active slots will run!
    </p>
    <div class="f">
      <label>Accounts List</label>
      <textarea id="bulk-text" rows="9" placeholder="100000001:password123&#10;100000002:password456&#10;100000003:password789" oninput="updateBulkCount()"></textarea>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;font-size:11px;color:#94a3b8">
      <span id="bulk-count-label">0 accounts detected</span>
      <span style="color:#60a5fa">Active slots login first</span>
    </div>
    <button type="button" class="sb" id="btn-submit-bulk" onclick="submitBulkAdd()">Import Accounts</button>
  </div>
</div>

<!-- CONFIRMATION MODAL -->
<div class="conf" id="cm">
  <div class="conf-box">
    <div class="conf-head" id="cm-t">Confirm</div>
    <div class="conf-msg" id="cm-m">Are you sure?</div>
    <div class="conf-btns">
      <button class="conf-yes" id="cm-y">Yes</button>
      <button class="conf-no" id="cm-n">No</button>
    </div>
  </div>
</div>

<script>
let currentFilter = 'all';
const selectedUids = new Set();
let cachedAccounts = [];
let cachedSettings = {};
const prevGainedMap = {};
const recentDiffMap = {};

function esc(s){if(s==null)return'';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}

function showConfirm(title, msg, yesText, noText){
  return new Promise(resolve=>{
    document.getElementById('cm-t').textContent = title;
    document.getElementById('cm-m').textContent = msg;
    document.getElementById('cm-y').textContent = yesText || 'Yes';
    document.getElementById('cm-n').textContent = noText || 'No';
    document.getElementById('cm-n').style.display = '';
    document.getElementById('cm').classList.add('on');
    const clean = () => {
      document.getElementById('cm').classList.remove('on');
      document.getElementById('cm-y').onclick = null;
      document.getElementById('cm-n').onclick = null;
    };
    document.getElementById('cm-y').onclick = () => { clean(); resolve(true); };
    document.getElementById('cm-n').onclick = () => { clean(); resolve(false); };
  });
}

function setFilter(flt){
  currentFilter = flt;
  document.querySelectorAll('.f-tab').forEach(b => {
    b.classList.toggle('active', b.dataset.filter === flt);
  });
  renderCards();
}

function updateSelectionUI(){
  document.getElementById('sel-count-num').textContent = selectedUids.size;
  const visible = getVisibleAccounts();
  const allChecked = visible.length > 0 && visible.every(a => selectedUids.has(String(a.uid)));
  const chkAll = document.getElementById('chk-all');
  if(chkAll) chkAll.checked = allChecked;
}

function toggleSelect(uid, checked){
  const k = String(uid);
  if(checked) selectedUids.add(k);
  else selectedUids.delete(k);
  updateSelectionUI();
  const card = document.querySelector(`.acc-card[data-uid="${k}"]`);
  if(card) card.classList.toggle('selected', checked);
}

function toggleSelectAll(checked){
  const visible = getVisibleAccounts();
  visible.forEach(a => {
    const k = String(a.uid);
    if(checked) selectedUids.add(k);
    else selectedUids.delete(k);
  });
  updateSelectionUI();
  renderCards();
}

function getVisibleAccounts(){
  return cachedAccounts.filter(acc => {
    if(currentFilter === 'all') return true;
    const st = (acc.status || '').toLowerCase();
    return st === currentFilter;
  });
}

function renderCards(){
  const grid = document.getElementById('grid');
  if(cachedAccounts.length === 0) selectedUids.clear();
  const visible = getVisibleAccounts();

  if(visible.length === 0){
    if(currentFilter === 'all'){
      grid.innerHTML = '<div class="empty-box"><p style="font-size:13px;color:#94a3b8;margin-bottom:12px">No accounts added yet.</p><button type="button" class="btn-add-accs" onclick="openBulkAdd()" style="padding:10px 24px;font-size:13px">+ Add Accounts (Unlimited)</button></div>';
    } else {
      grid.innerHTML = '<div class="empty-box"><p>No accounts match the "' + currentFilter.toUpperCase() + '" filter.</p></div>';
    }
    updateSelectionUI();
    return;
  }

  const expTarget = parseInt(cachedSettings.exp_limit || 0);
  const lvlTarget = parseInt(cachedSettings.level_limit || 0);
  const hasTarget = expTarget > 0 || lvlTarget > 0;

  let html = '';
  visible.forEach(acc => {
    const uid = esc(acc.uid);
    const nickname = esc(acc.nickname || 'Player');
    const initial = nickname.charAt(0).toUpperCase() || 'P';
    const region = esc(acc.region || 'BD');
    const status = (acc.status || 'WAITING').toUpperCase();
    const mode = esc(acc.mode || 'AUTO');
    const curExp = (acc.current_exp || 0);
    const gained = (acc.gained_exp || 0);
    const matches = (acc.matches_played || 0);
    const level = (acc.level || 1);
    const isSelected = selectedUids.has(String(acc.uid));
    const isPaused = status === 'PAUSED';

    // Green + Number difference detection
    const diffEntry = recentDiffMap[acc.uid];
    let gainBadgeHtml = '';
    if(diffEntry && diffEntry.gain > 0){
      gainBadgeHtml = '<span class="gain-pop-green">+' + diffEntry.gain.toLocaleString() + '</span>';
    } else if(acc.last_gain > 0 && acc.last_gain_time && ((Date.now() / 1000) - acc.last_gain_time < 20)){
      gainBadgeHtml = '<span class="gain-pop-green">+' + acc.last_gain.toLocaleString() + '</span>';
    }

    // Status class mapping
    let stCls = 'status-waiting';
    if(status === 'RUNNING' || status === 'LIVE') stCls = 'status-running';
    else if(status === 'DONE') stCls = 'status-done';
    else if(status === 'PAUSED') stCls = 'status-paused';
    else if(status === 'ERROR') stCls = 'status-error';
    else if(status === 'OFFLINE') stCls = 'status-offline';

    // Progress and ETA
    const etaFmt = acc.eta_formatted || '--';
    const progPct = Math.min(100, Math.max(0, acc.progress_pct || 0));

    html += '<div class="acc-card ' + (isSelected ? 'selected' : '') + '" data-uid="' + uid + '">';
    
    // Top Row
    html += '<div class="card-top">';
    html += '<div class="card-top-left">';
    html += '<input type="checkbox" class="card-chk" ' + (isSelected ? 'checked' : '') + ' onchange="toggleSelect(&quot;' + uid + '&quot;, this.checked)">';
    html += '<span class="status-pill ' + stCls + '"><span class="dot"></span>' + status + '</span>';
    html += '</div>';
    html += '<div class="top-right" style="display:flex;gap:4px">';
    html += '<span class="tag-pill">' + region + '</span>';
    html += '<span class="tag-pill tag-mode">' + mode + '</span>';
    html += '</div>';
    html += '</div>';

    // Profile Row
    html += '<div class="card-profile">';
    html += '<div class="avatar-small">' + initial + '</div>';
    html += '<div class="prof-info">';
    html += '<div class="prof-name-row"><span class="prof-name">' + nickname + '</span><span class="lvl-badge">Lv.' + level + '</span></div>';
    html += '<div class="prof-uid">UID: ' + uid + '</div>';
    html += '</div>';
    html += '</div>';

    // Target Box if set
    if(hasTarget){
      html += '<div class="card-target-box">';
      html += '<div class="target-labels"><span class="lbl">Progress ' + progPct + '%</span><span class="eta">⏱ ETA: ' + etaFmt + '</span></div>';
      html += '<div class="prog-bar"><div class="prog-fill" style="width:' + progPct + '%"></div></div>';
      html += '</div>';
    }

    // Stats Grid
    html += '<div class="card-stats">';
    html += '<div class="c-stat"><div class="l">EXP</div><div class="v">' + curExp.toLocaleString() + '</div></div>';
    html += '<div class="c-stat"><div class="l">Gained</div><div class="v g"><span>' + gained.toLocaleString() + '</span>' + (gainBadgeHtml ? ' ' + gainBadgeHtml : '') + '</div></div>';
    html += '<div class="c-stat"><div class="l">Matches</div><div class="v">' + matches + '</div></div>';
    html += '</div>';

    // Action buttons
    html += '<div class="card-actions">';
    html += '<button type="button" class="c-btn" title="Pause / Resume" onclick="singleAction(&quot;' + uid + '&quot;, &quot;' + (isPaused ? 'resume' : 'pause') + '&quot;)">' + (isPaused ? '▶ Run' : '⏸ Pause') + '</button>';
    html += '<button type="button" class="c-btn" title="Relogin" onclick="singleAction(&quot;' + uid + '&quot;, &quot;relogin&quot;)">🔄 Relogin</button>';
    html += '<button type="button" class="c-btn" title="Toggle Queue" onclick="singleAction(&quot;' + uid + '&quot;, &quot;' + (status === 'RUNNING' ? 'move_waiting' : 'move_running') + '&quot;)">' + (status === 'RUNNING' ? '⏳ Wait' : '▶ Slot') + '</button>';
    html += '<button type="button" class="c-btn del" title="Delete" onclick="deleteSingleAccount(&quot;' + uid + '&quot;)">🗑</button>';
    html += '</div>';

    html += '</div>';
  });

  grid.innerHTML = html;
  updateSelectionUI();
}

function updateControlsUI(st){
  cachedSettings = st || {};

  // Daily Autoplay
  const autoBtn = document.getElementById('btn-daily-autoplay');
  const autoVal = document.getElementById('val-daily-autoplay');
  if(st.daily_autoplay){
    autoBtn.className = 'toggle-btn on';
    autoVal.textContent = 'ON';
  } else {
    autoBtn.className = 'toggle-btn off';
    autoVal.textContent = 'OFF';
  }

  // Days
  if(st.days && document.activeElement !== document.getElementById('inp-days')) document.getElementById('inp-days').value = st.days;

  // Active Slots
  if(st.active_slots && document.activeElement !== document.getElementById('inp-slots')) document.getElementById('inp-slots').value = st.active_slots;

  // Retry
  if(st.login_retry && document.activeElement !== document.getElementById('inp-retry')) document.getElementById('inp-retry').value = st.login_retry;

  // Daily Limit
  if(st.daily_limit !== undefined && document.activeElement !== document.getElementById('inp-daily-limit')) document.getElementById('inp-daily-limit').value = st.daily_limit;

  // All Bots
  const allBtn = document.getElementById('btn-all-bots');
  const allVal = document.getElementById('val-all-bots');
  if(st.all_bots !== false){
    allBtn.className = 'toggle-btn on';
    allVal.textContent = 'ON';
  } else {
    allBtn.className = 'toggle-btn off';
    allVal.textContent = 'OFF';
  }

  // Target Delete
  const delBtn = document.getElementById('btn-target-delete');
  const delVal = document.getElementById('val-target-delete');
  if(st.target_delete){
    delBtn.className = 'toggle-btn on';
    delVal.textContent = 'ON';
  } else {
    delBtn.className = 'toggle-btn off';
    delVal.textContent = 'OFF';
  }

  // EXP Limit
  if(st.exp_limit !== undefined){
    if(document.activeElement !== document.getElementById('inp-exp-limit')) document.getElementById('inp-exp-limit').value = st.exp_limit;
    const expHint = document.getElementById('hint-exp-limit');
    if(parseInt(st.exp_limit) > 0) expHint.textContent = 'Limit: ' + parseInt(st.exp_limit).toLocaleString() + ' EXP (Target Complete)';
    else expHint.textContent = 'No limit (accounts are never auto-deleted)';
  }

  // Level Limit
  if(st.level_limit !== undefined){
    if(document.activeElement !== document.getElementById('inp-level-limit')) document.getElementById('inp-level-limit').value = st.level_limit;
    const lvlHint = document.getElementById('hint-level-limit');
    if(parseInt(st.level_limit) > 0) lvlHint.textContent = 'Target: Level ' + st.level_limit;
    else lvlHint.textContent = 'No limit (accounts are never auto-deleted)';
  }

  // Game Mode
  const curMode = (st.game_mode || 'AUTO').toUpperCase();
  document.getElementById('mode-btn-auto').classList.toggle('on', curMode === 'AUTO');
  document.getElementById('mode-btn-br').classList.toggle('on', curMode === 'ONLY_BR');
  document.getElementById('mode-btn-cs').classList.toggle('on', curMode === 'ONLY_CS');
}

function updateCountsUI(counts){
  counts = counts || {};
  document.getElementById('cnt-all').textContent = counts.all || 0;
  document.getElementById('cnt-running').textContent = counts.running || 0;
  document.getElementById('cnt-waiting').textContent = counts.waiting || 0;
  document.getElementById('cnt-done').textContent = counts.done || 0;
  document.getElementById('cnt-paused').textContent = counts.paused || 0;
  document.getElementById('cnt-error').textContent = counts.error || 0;
  document.getElementById('cnt-offline').textContent = counts.offline || 0;
}

function updateSystemUI(sys, pingMs){
  sys = sys || {};
  if(pingMs) document.getElementById('hdr-ping').textContent = pingMs + 'ms';
  if(sys.ram_used_mb && sys.ram_total_mb){
    document.getElementById('hdr-ram').textContent = 'RAM ' + sys.ram_used_mb + '/' + sys.ram_total_mb + 'MB (' + (sys.ram_pct || 63) + '%)';
  }
  if(sys.cpu_pct !== undefined){
    document.getElementById('hdr-cpu').textContent = 'CPU ' + sys.cpu_pct + '%';
  }
  if(sys.workers_count !== undefined){
    document.getElementById('hdr-workers').textContent = 'Workers ' + sys.workers_count;
  }
}

function fmtLeft(s){
  if(!s || s >= 100000000) return 'Unlimited';
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  if(h > 0) return h + 'h ' + m + 'm';
  return m + 'm';
}

async function fetchStats(){
  const t0 = performance.now();
  try{
    const r = await fetch('/api/stats');
    const pingMs = Math.round(performance.now() - t0);
    if(r.status === 401){ return; }
    const d = await r.json();

    // Detect EXP diff for the green + number badge
    const nowTs = Date.now();
    (d.accounts || []).forEach(acc => {
      const prev = prevGainedMap[acc.uid];
      if(prev !== undefined && acc.gained_exp > prev){
        const diff = acc.gained_exp - prev;
        recentDiffMap[acc.uid] = { gain: diff, time: nowTs };
      }
      prevGainedMap[acc.uid] = acc.gained_exp;
    });

    // Auto-clear gains older than 15 seconds
    for(const uid in recentDiffMap){
      if(nowTs - recentDiffMap[uid].time > 15000){
        delete recentDiffMap[uid];
      }
    }

    cachedAccounts = d.accounts || [];
    updateControlsUI(d.settings);
    updateCountsUI(d.counts);
    updateSystemUI(d.system, pingMs);

    document.getElementById('val-total-eta').textContent = d.total_eta_formatted || '--';
    if(document.getElementById('ui-u')) document.getElementById('ui-u').textContent = d.username || 'Admin';
    if(document.getElementById('ui-t')) document.getElementById('ui-t').textContent = 'ONLINE';

    renderCards();
  }catch(ex){
    console.error('fetchStats error:', ex);
  }
}

// Settings Handlers
function toggleDailyAutoplay(){
  cachedSettings.daily_autoplay = !cachedSettings.daily_autoplay;
  updateControlsUI(cachedSettings);
  saveSettings();
}
function adjustSlots(delta){
  const inp = document.getElementById('inp-slots');
  let val = Math.max(1, (parseInt(inp.value) || 1) + delta);
  inp.value = val;
  cachedSettings.active_slots = val;
  saveSettings();
}
function toggleAllBots(){
  cachedSettings.all_bots = !(cachedSettings.all_bots !== false);
  updateControlsUI(cachedSettings);
  saveSettings();
}
function toggleTargetDelete(){
  cachedSettings.target_delete = !cachedSettings.target_delete;
  updateControlsUI(cachedSettings);
  saveSettings();
}
function setExpLimit(){
  const raw = document.getElementById('inp-exp-limit').value.trim();
  const val = raw === '' ? 0 : Math.max(0, parseInt(raw) || 0);
  cachedSettings.exp_limit = val;
  updateControlsUI(cachedSettings);
  saveSettings();
}
function setLevelLimit(){
  const raw = document.getElementById('inp-level-limit').value.trim();
  const val = raw === '' ? 21 : Math.max(0, parseInt(raw) || 0);
  cachedSettings.level_limit = val;
  updateControlsUI(cachedSettings);
  saveSettings();
}
function setGameMode(mode){
  cachedSettings.game_mode = mode;
  updateControlsUI(cachedSettings);
  saveSettings();
}

async function saveSettings(){
  const rawDays = document.getElementById('inp-days').value.trim();
  const rawSlots = document.getElementById('inp-slots').value.trim();
  const rawRetry = document.getElementById('inp-retry').value.trim();
  const rawDaily = document.getElementById('inp-daily-limit').value.trim();
  const rawExp = document.getElementById('inp-exp-limit').value.trim();
  const rawLvl = document.getElementById('inp-level-limit').value.trim();
  const payload = {
    settings: {
      daily_autoplay: cachedSettings.daily_autoplay || false,
      days: rawDays === '' ? 1 : Math.max(1, parseInt(rawDays) || 1),
      active_slots: rawSlots === '' ? 10 : Math.max(1, parseInt(rawSlots) || 10),
      login_retry: rawRetry === '' ? 3 : Math.max(1, parseInt(rawRetry) || 3),
      daily_limit: rawDaily === '' ? 60000 : Math.max(0, parseInt(rawDaily) || 0),
      all_bots: cachedSettings.all_bots !== false,
      target_delete: cachedSettings.target_delete || false,
      exp_limit: rawExp === '' ? 0 : Math.max(0, parseInt(rawExp) || 0),
      level_limit: rawLvl === '' ? 21 : Math.max(0, parseInt(rawLvl) || 0),
      game_mode: cachedSettings.game_mode || 'AUTO'
    }
  };
  try{
    const r = await fetch('/api/settings/save', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload)
    });
    if(r.status === 401){ return; }
    fetchStats();
  }catch(e){}
}

// Bulk Actions
async function bulkAction(act){
  if(selectedUids.size === 0){
    alert('Please select at least one account first.');
    return;
  }
  if(act === 'delete'){
    const ok = await showConfirm('Delete Accounts', 'Are you sure you want to delete ' + selectedUids.size + ' selected account(s)?', 'Delete', 'Cancel');
    if(!ok) return;
  }
  const uids = Array.from(selectedUids);
  try{
    const r = await fetch('/api/account/bulk-action', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ action: act, uids: uids })
    });
    if(r.status === 401){ return; }
    if(act === 'delete') selectedUids.clear();
    fetchStats();
  }catch(e){}
}

async function singleAction(uid, act){
  try{
    const r = await fetch('/api/account/bulk-action', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ action: act, uids: [String(uid)] })
    });
    if(r.status === 401){ return; }
    if(act === 'delete'){
      selectedUids.delete(String(uid));
      updateSelectionUI();
    }
    fetchStats();
  }catch(e){}
}

async function deleteSingleAccount(uid){
  const ok = await showConfirm('Delete Account', 'Are you sure you want to delete account ' + uid + '?', 'Delete', 'Cancel');
  if(!ok) return;
  singleAction(uid, 'delete');
}

async function confirmClearAll(){
  const ok = await showConfirm('Clear All IDs', 'Are you sure you want to DELETE ALL IDs? All accounts will be permanently removed.', 'Yes, Clear All', 'Cancel');
  if(!ok) return;
  try{
    const r = await fetch('/api/account/clear-all', {method: 'POST'});
    if(r.status === 401){ return; }
    selectedUids.clear();
    fetchStats();
  }catch(e){}
}

// Bulk Add Modal Handlers
function openBulkAdd(){
  document.getElementById('modal-bulk-add').classList.add('on');
  document.getElementById('bulk-err').classList.remove('on');
  const txt = document.getElementById('bulk-text');
  txt.value = '';
  setTimeout(() => txt.focus(), 50);
  updateBulkCount();
}
function closeBulkAdd(){
  document.getElementById('modal-bulk-add').classList.remove('on');
}
function updateBulkCount(){
  const txt = document.getElementById('bulk-text').value.trim();
  const count = txt ? txt.split(String.fromCharCode(10)).filter(l => l.trim().length > 0 && !l.trim().startsWith('#')).length : 0;
  document.getElementById('bulk-count-label').textContent = count + ' accounts detected';
}
async function submitBulkAdd(){
  const txt = document.getElementById('bulk-text').value.trim();
  const err = document.getElementById('bulk-err');
  err.classList.remove('on');
  if(!txt){
    err.textContent = 'Please enter at least one account (uid:password or token).';
    err.classList.add('on');
    return;
  }
  const btn = document.getElementById('btn-submit-bulk');
  btn.disabled = true;
  btn.textContent = 'Importing...';
  try{
    const r = await fetch('/api/account/bulk-add', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ text: txt })
    });
    const d = await r.json().catch(() => null);
    if(r.ok && d && d.status === 'ok'){
      closeBulkAdd();
      await fetchStats();
    } else {
      err.textContent = (d && d.error) || ('Server returned HTTP ' + r.status);
      err.classList.add('on');
    }
  }catch(ex){
    err.textContent = 'Network error while adding accounts: ' + ex.message;
    err.classList.add('on');
  }finally{
    btn.disabled = false;
    btn.textContent = 'Import Accounts';
  }
}

document.getElementById('rf').addEventListener('click', async () => {
  const b = document.getElementById('rf');
  b.classList.add('sp');
  await fetchStats();
  setTimeout(() => b.classList.remove('sp'), 700);
});

fetchStats();
setInterval(fetchStats, 3000);
</script>
</body>
</html>
"""

DASHBOARD_HTML = DASHBOARD_HTML.replace("__ICON_REFRESH__", _icon("refresh", "currentColor", 14))

# Standalone Dashboard & Aliases (Login eliminated completely)
LOGIN_HTML = DASHBOARD_HTML
HOME_HTML = DASHBOARD_HTML
PLANS_HTML = DASHBOARD_HTML
EXPIRED_HTML = DASHBOARD_HTML
ADMIN_LOGIN_HTML = DASHBOARD_HTML
ADMIN_PANEL_HTML = DASHBOARD_HTML

ALL_TEMPLATES = {
    'home': HOME_HTML,
    'login': LOGIN_HTML,
    'plans': PLANS_HTML,
    'dashboard': DASHBOARD_HTML,
    'expired': EXPIRED_HTML,
    'admin_login': ADMIN_LOGIN_HTML,
    'admin_panel': ADMIN_PANEL_HTML,
}
