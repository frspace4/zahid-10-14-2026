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


# ==================== HOME (Landing) ====================
HOME_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>h X LevelUp - Free Fire Automation</title>
""" + _FONTS + """
<style>
""" + _CSS + """
html{scroll-behavior:smooth}
html,body{height:100%}
body{background:#050505;min-height:100vh;position:relative;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:
  linear-gradient(rgba(255,255,255,0.015) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,255,255,0.015) 1px,transparent 1px);
  background-size:60px 60px;pointer-events:none;z-index:0;
  mask-image:radial-gradient(ellipse at 50% 40%,#000 20%,transparent 75%);
  -webkit-mask-image:radial-gradient(ellipse at 50% 40%,#000 20%,transparent 75%)}

/* Announcement */
.ann{position:relative;z-index:5;background:#fff;color:#000;padding:9px 40px 9px 14px;text-align:center;font-size:12px;font-weight:600;font-family:'Inter',sans-serif}
.ann a{color:#000;text-decoration:underline;font-weight:800}
.ann .cls{position:absolute;right:12px;top:50%;transform:translateY(-50%);background:transparent;border:none;cursor:pointer;color:#000;font-size:16px;line-height:1;padding:4px}

/* Header */
.hdr{position:relative;z-index:5;display:flex;align-items:center;justify-content:space-between;padding:14px 18px;border-bottom:1px solid #151515}
.hlogo{display:flex;align-items:center;gap:10px}
.hshield{width:34px;height:34px;display:inline-flex;align-items:center;justify-content:center}
.hshield svg{width:34px;height:34px;stroke:#fff;fill:none;stroke-width:1.8}
.hname{font-family:'Inter',sans-serif;font-size:14px;font-weight:800;letter-spacing:2.5px;color:#fff}
.hbell{background:transparent;border:none;cursor:pointer;padding:6px;color:#fff}
.hbell svg{width:20px;height:20px;stroke:#fff;fill:none;stroke-width:1.8}

/* Status pill */
.status{position:relative;z-index:5;display:flex;justify-content:center;padding:16px 18px 0}
.spill{display:inline-flex;align-items:center;gap:8px;background:#0d0d0d;border:1px solid #1c1c1c;border-radius:24px;padding:7px 14px 7px 11px;font-family:'Inter',sans-serif;font-size:11px;font-weight:600;color:#b8b8b8}
.spill .dot{width:7px;height:7px;border-radius:50%;background:#22c55e;box-shadow:0 0 8px #22c55e;animation:pl 1.4s infinite}
.spill .mut{color:#5a5a5a;font-weight:400;margin-left:2px}
@keyframes pl{0%,100%{opacity:1}50%{opacity:0.4}}

/* Hero */
.hero{position:relative;z-index:5;padding:50px 22px 20px;max-width:640px;margin:0 auto;text-align:center}
.hero h1{font-family:'Inter',sans-serif;font-size:26px;font-weight:800;letter-spacing:1.5px;margin-bottom:36px;
  background:linear-gradient(90deg,#22d3ee,#a78bfa,#22d3ee);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 24px rgba(34,211,238,0.35));}
.hero p{font-family:'Inter',sans-serif;font-size:17px;font-weight:500;line-height:1.65;color:#b8b8b8;letter-spacing:0.2px}
.hero p + p{margin-top:14px}

/* CTA buttons */
.ctas{position:relative;z-index:5;display:flex;gap:12px;justify-content:center;padding:24px 18px 50px;flex-wrap:wrap;max-width:440px;margin:0 auto}
.cbtn{flex:1;min-width:140px;padding:14px 20px;border-radius:10px;font-family:'Inter',sans-serif;font-size:14px;font-weight:800;letter-spacing:0.5px;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:8px;border:1px solid transparent;transition:all 0.2s}
.cb-white{background:#fff;color:#000}
.cb-white:hover{background:#e5e5e5}
.cb-out{background:transparent;border-color:#2a2a2a;color:#fff}
.cb-out:hover{border-color:#555;background:#0d0d0d}
.cbtn svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2.2}

/* Pricing section */
.psec{position:relative;z-index:5;max-width:1200px;margin:0 auto;padding:0 18px 80px;scroll-margin-top:20px}
.ptitle{text-align:center;font-family:'Inter',sans-serif;font-size:24px;font-weight:800;letter-spacing:1px;color:#fff;margin-bottom:8px}
.psub{text-align:center;font-size:11px;color:#7a7a7a;letter-spacing:3px;text-transform:uppercase;margin-bottom:14px;font-weight:600}
.pnote{text-align:center;font-size:11px;color:#7a8ba0;max-width:560px;margin:0 auto 30px;line-height:1.6;padding:10px 16px;background:rgba(59,130,246,0.05);border:1px solid rgba(59,130,246,0.15);border-radius:10px}
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
@media(max-width:700px){.pgrid{grid-template-columns:1fr}}

.pc{background:#0b0b0e;border:1.5px solid #1f1f24;border-radius:18px;padding:32px 22px 22px;position:relative;display:flex;flex-direction:column;transition:all 0.3s}
.pc.blue{border-color:rgba(59,130,246,0.45)}
.pc.blue:hover{border-color:#3b82f6;box-shadow:0 0 40px rgba(59,130,246,0.25);transform:translateY(-4px)}
.pc.purple{border-color:rgba(139,92,246,0.5)}
.pc.purple:hover{border-color:#8b5cf6;box-shadow:0 0 40px rgba(139,92,246,0.3);transform:translateY(-4px)}
.pc.gold{border-color:rgba(245,158,11,0.5)}
.pc.gold:hover{border-color:#f59e0b;box-shadow:0 0 40px rgba(245,158,11,0.25);transform:translateY(-4px)}
.ribbon{position:absolute;top:-11px;right:20px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:1.5px;padding:5px 12px;border-radius:20px;text-transform:uppercase;box-shadow:0 4px 20px rgba(139,92,246,0.5)}
.pi{width:64px;height:64px;margin:0 auto 20px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.pc.blue .pi{background:rgba(59,130,246,0.08);border:1.5px solid rgba(59,130,246,0.35);color:#60a5fa}
.pc.purple .pi{background:rgba(139,92,246,0.08);border:1.5px solid rgba(139,92,246,0.4);color:#a78bfa}
.pc.gold .pi{background:rgba(245,158,11,0.08);border:1.5px solid rgba(245,158,11,0.4);color:#fbbf24}
.pi svg{width:28px;height:28px}
.pn{text-align:center;font-family:'Inter',sans-serif;font-size:20px;font-weight:800;letter-spacing:5px;margin-bottom:14px;color:#fff;text-transform:uppercase}
.pl{display:flex;justify-content:center;align-items:center;gap:10px;margin-bottom:8px}
.op{font-family:'Inter',sans-serif;font-size:15px;font-weight:700;color:#4a4a4a;text-decoration:line-through}
.deal{background:#dc2626;color:#fff;font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:1.2px;padding:3px 8px;border-radius:5px}
.pm{text-align:center;font-family:'Inter',sans-serif;font-size:48px;font-weight:900;letter-spacing:-1px;margin-bottom:26px;line-height:1;color:#fff}
.pm .cur{font-size:26px;font-weight:700;vertical-align:top;line-height:1;display:inline-block;margin-right:2px}
.feats{list-style:none;margin-bottom:22px;flex:1}
.feats li{display:flex;align-items:flex-start;gap:10px;padding:7px 0;font-size:13px;color:#d8d8dd;line-height:1.45;font-weight:500}
.feats li .ic{flex-shrink:0;width:18px;height:18px;display:flex;align-items:center;justify-content:center;margin-top:2px;color:#22c55e}
.feats li .ic svg{width:14px;height:14px}
.bb{width:100%;padding:13px;border-radius:10px;font-family:'Inter',sans-serif;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;border:none;cursor:pointer;transition:all 0.25s;color:#fff}
.pc.blue .bb{background:linear-gradient(135deg,#3b82f6,#2563eb);box-shadow:0 6px 24px rgba(59,130,246,0.3)}
.pc.purple .bb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);box-shadow:0 6px 24px rgba(139,92,246,0.35)}
.pc.gold .bb{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 6px 24px rgba(245,158,11,0.3);color:#000}
.an{text-align:center;font-size:10px;color:#4a4a4a;margin-top:10px;letter-spacing:0.5px;font-weight:500}

/* Telegram float */
.tg{position:fixed;right:18px;bottom:18px;width:52px;height:52px;border-radius:50%;background:#22a7e8;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 28px rgba(34,167,232,0.5);cursor:pointer;z-index:20;border:none;text-decoration:none}
.tg svg{width:26px;height:26px;fill:#fff}

/* Maintenance popup */
.mtop{position:fixed;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);z-index:100;display:none;align-items:center;justify-content:center;padding:18px}
.mtop.on{display:flex}
.mbox{background:#141414;border:1px solid #262626;border-radius:18px;padding:22px;max-width:440px;width:100%;position:relative;font-family:'Inter',sans-serif}
.mh-row{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:24px}
.mh-row h3{font-size:17px;font-weight:700;color:#fff;letter-spacing:0.2px}
.mclose{width:34px;height:34px;border-radius:50%;border:1px solid #2a2a2a;background:transparent;color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.mclose:hover{background:#1e1e1e}
.mclose svg{width:16px;height:16px;stroke:#fff;fill:none;stroke-width:2}
.micon{width:56px;height:56px;margin:0 auto 18px;display:flex;align-items:center;justify-content:center}
.micon svg{width:56px;height:56px;stroke:#fff;fill:none;stroke-width:1.5}
.mtitle{text-align:center;font-size:19px;font-weight:800;color:#fff;margin-bottom:14px;letter-spacing:0.3px}
.mtext{text-align:center;font-size:13px;line-height:1.65;color:#a8a8a8;margin-bottom:22px}
.mbtn{width:100%;padding:14px;border-radius:10px;background:#fff;color:#000;border:none;font-family:'Inter',sans-serif;font-size:14px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;text-decoration:none}
.mbtn:hover{background:#e5e5e5}
</style>
</head>
<body>

<div class="ann" id="ann">
IND server is disabled &mdash; please wait patiently! <a href="#pricing">Learn More</a>
<button class="cls" onclick="document.getElementById('ann').style.display='none'">✕</button>
</div>

<div class="hdr">
<div class="hlogo">
<span class="hshield"><svg viewBox="0 0 24 24"><path d="M12 2L4 5v6c0 5 3.5 9.5 8 11 4.5-1.5 8-6 8-11V5l-8-3z"/><path d="M9 12l2 2 4-4"/></svg></span>
<span class="hname">hh X LevelUp</span>
</div>
<button class="hbell"><svg viewBox="0 0 24 24"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></button>
</div>

<div class="status">
<span class="spill"><span class="dot"></span> System Operational <span class="mut">0ms</span></span>
</div>

<div class="hero">
<h1>hh X LEVEL UP</h1>
<p>Fast, reliable Free Fire level-up automation built for players who want results without the grind. Simple setup, real progress.</p>
<p>Level up your account faster &mdash; stay ahead of the competition.</p>
</div>

<div class="ctas">
<a href="/dashboard" class="cbtn cb-white">Get Started <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a>
<a href="#pricing" class="cbtn cb-out">Pricing <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></a>
</div>

<!-- Pricing -->
<div class="psec" id="pricing">
<div class="ptitle">Choose Your Plan</div>
<div class="psub">Works On All Servers</div>
<div class="pnote">All plans work globally across every Free Fire server &mdash; IND, BD, EUROPE, SG, TH, PH, VN, MY, ID, HK, TW and more. Price shown in USD.</div>
<div class="pgrid" id="pgrid"></div>
</div>

<a class="tg" href="https://t.me/Nxt_hh_s" target="_blank"><svg viewBox="0 0 24 24"><path d="M9.78 18.65l.28-4.23 7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3 3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"/></svg></a>

<div class="mtop" id="maint">
<div class="mbox">
<div class="mh-row">
<h3>Important Update</h3>
<button class="mclose" onclick="document.getElementById('maint').classList.remove('on')"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
</div>
<div class="micon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="8 12 11 15 16 9"/></svg></div>
<div class="mtitle">IND Server Maintenance</div>
<div class="mtext">Due To Game Restrictions In IND Server, Our Level Up System Can Only Farm 5K Exp Per Day. So We Decided To Close IND Server Until Our Devs Fix This. We Will Be Back Online For IND Server Soon.</div>
<a class="mbtn" href="https://t.me/Nxt_hh_s" target="_blank">Chat Now</a>
</div>
</div>

<script>
const PLANS=[
{id:'starting',name:'STARTING',style:'blue',icon:'bolt',hours:24,slots:3,price:'1',old:'2',pop:false},
{id:'basic',name:'BASIC',style:'purple',icon:'star',hours:48,slots:3,price:'2',old:'4',pop:true},
{id:'premium',name:'PREMIUM',style:'gold',icon:'crown',hours:72,slots:4,price:'2.5',old:'6',pop:false}
];
const TG='Nxt_hh_s';
const ICONS={
bolt:'__SVG_BOLT__',
star:'__SVG_STAR__',
crown:'__SVG_CROWN__',
check:'__SVG_CHECK__'
};

function feat(p){
const d=p.hours>=24?Math.round(p.hours/24)+' Day'+(p.hours>=48?'s':''):p.hours+' Hours';
const sp=p.id==='premium'?'Fastest Leveling Speed Available':'Fast Leveling Performance';
const off=p.id==='premium'?'Runs 24/7 — No Need To Stay Online':'Runs While You Are Offline';
return[
'Access To The Panel For '+d,
sp,
'Run Multiple Accounts At Once',
'Restart & Manage Accounts Anytime',
off,
'Telegram Payment Support & Quick Help',
p.slots+' Concurrent Account'+(p.slots>1?'s':'')
];
}

function render(){
const g=document.getElementById('pgrid');
let h='';
PLANS.forEach(p=>{
let fh='';
feat(p).forEach(t=>{fh+='<li><span class="ic">'+ICONS.check+'</span><span>'+t+'</span></li>';});
h+='<div class="pc '+p.style+'">';
if(p.pop)h+='<div class="ribbon">Most Popular</div>';
h+='<div class="pi">'+ICONS[p.icon]+'</div>';
h+='<div class="pn">'+p.name+'</div>';
h+='<div class="pl"><span class="op">$'+p.old+'</span><span class="deal">Deal</span></div>';
h+='<div class="pm"><span class="cur">$</span>'+p.price+'</div>';
h+='<ul class="feats">'+fh+'</ul>';
h+='<button class="bb" onclick="buy(\\''+p.id+'\\')">Buy '+p.name+'</button>';
h+='<div class="an">Instant Activation After Payment</div>';
h+='</div>';
});
g.innerHTML=h;
}

function buy(id){
const p=PLANS.find(x=>x.id===id);
let m='Hi, I Want To Buy The '+p.name+' Plan.\\n\\nPlan: $'+p.price+'\\nDuration: '+p.hours+' Hours\\nSlots: '+p.slots+'\\n\\nPlease Send Payment Details.';
window.open('https://t.me/'+TG+'?text='+encodeURIComponent(m),'_blank');
}
render();

/* Smooth scroll for #pricing */
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',e=>{
    const id=a.getAttribute('href');
    if(id.length>1){
      const el=document.querySelector(id);
      if(el){
        e.preventDefault();
        el.scrollIntoView({behavior:'smooth',block:'start'});
      }
    }
  });
});

/* Maintenance popup — every reload */
document.getElementById('maint').classList.add('on');
document.getElementById('maint').addEventListener('click',e=>{
  if(e.target.id==='maint')document.getElementById('maint').classList.remove('on');
});
</script>
</body>
</html>
"""

HOME_HTML = HOME_HTML.replace("__SVG_BOLT__", _icon("bolt_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_STAR__", _icon("star_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_CROWN__", _icon("crown_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_CHECK__", _icon("check", "#22c55e", 14).replace('"', '\\"'))

# ==================== LOGIN ====================
LOGIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Login - hh X Level Up</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:#0a0a0a;display:flex;align-items:center;justify-content:center;padding:20px;min-height:100vh;position:relative}
body::before{content:'';position:absolute;inset:0;background:
  linear-gradient(rgba(255,255,255,0.015) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,255,255,0.015) 1px,transparent 1px);
  background-size:60px 60px;pointer-events:none;mask-image:radial-gradient(ellipse at center,#000 20%,transparent 80%);
  -webkit-mask-image:radial-gradient(ellipse at center,#000 20%,transparent 80%)}

.wrap{width:100%;max-width:440px;position:relative;z-index:1}
.brand{display:flex;align-items:center;justify-content:center;gap:12px;margin-bottom:60px}
.shield{
  width:36px;height:36px;
  display:inline-flex;align-items:center;justify-content:center;
}
.shield svg{width:36px;height:36px;stroke:#fff;fill:none;stroke-width:1.8}
.brand-txt{font-family:'Inter',sans-serif;font-size:18px;font-weight:800;letter-spacing:3px;color:#fff}
.brand-txt .dot{color:#555;font-weight:700}

.welcome{text-align:center;margin-bottom:36px}
.welcome h1{font-family:'Inter',sans-serif;font-size:28px;font-weight:700;letter-spacing:-0.5px;color:#fff;margin-bottom:8px}
.welcome p{font-size:13px;color:#7a7a7a;font-weight:400}

.err{background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.3);color:#ef4444;padding:11px;border-radius:10px;font-size:12px;margin-bottom:16px;display:none;text-align:center}
.err.on{display:block}

.f{margin-bottom:20px}
.f label{display:block;font-size:13px;font-weight:700;color:#fff;margin-bottom:9px;text-align:center}
.iw{position:relative}
.iw svg.lft{position:absolute;left:16px;top:50%;transform:translateY(-50%);width:18px;height:18px;stroke:#6a6a6a;fill:none;stroke-width:1.8;pointer-events:none}
.iw svg.rgt{position:absolute;right:16px;top:50%;transform:translateY(-50%);width:18px;height:18px;stroke:#6a6a6a;fill:none;stroke-width:1.8;cursor:pointer;transition:stroke 0.2s}
.iw svg.rgt:hover{stroke:#fff}
.f input{
  width:100%;background:transparent;
  border:1px solid #2a2a2a;border-radius:10px;
  padding:15px 46px;
  color:#fff;font-size:14px;
  font-family:'Inter',sans-serif;font-weight:500;
  outline:none;transition:all 0.2s;
}
.f input::placeholder{color:#4a4a4a;font-weight:400}
.f input:focus{border-color:#555;background:rgba(255,255,255,0.02)}

.remember{display:flex;align-items:center;justify-content:center;gap:10px;margin:24px 0 22px}
.remember input[type=checkbox]{
  appearance:none;-webkit-appearance:none;
  width:20px;height:20px;border-radius:5px;
  border:1.5px solid #444;background:transparent;
  cursor:pointer;position:relative;transition:all 0.2s;flex-shrink:0;
}
.remember input[type=checkbox]:checked{background:#fff;border-color:#fff}
.remember input[type=checkbox]:checked::after{
  content:'';position:absolute;left:6px;top:2px;
  width:6px;height:11px;
  border:solid #000;border-width:0 2px 2px 0;
  transform:rotate(45deg);
}
.remember label{font-size:14px;color:#b8b8b8;cursor:pointer;font-weight:500}

.btn{
  width:100%;padding:17px;border-radius:10px;
  background:#8a8a8a;color:#0a0a0a;
  border:none;cursor:pointer;
  font-family:'Inter',sans-serif;
  font-size:15px;font-weight:700;
  letter-spacing:0.3px;
  display:flex;align-items:center;justify-content:center;gap:10px;
  transition:all 0.2s;
}
.btn:hover{background:#a0a0a0}
.btn svg{width:18px;height:18px;stroke:#0a0a0a;fill:none;stroke-width:2}
.btn:disabled{opacity:0.6;cursor:not-allowed}

.foot{text-align:center;margin-top:28px;font-size:13px;color:#6a6a6a}
.foot a{color:#fff;text-decoration:none;font-weight:600;border-bottom:1px solid #333;padding-bottom:1px}
.foot a:hover{border-color:#fff}
</style>
</head>
<body>
<div class="wrap">

<div class="brand">
<span class="shield">
<svg viewBox="0 0 24 24"><path d="M12 2L4 5v6c0 5 3.5 9.5 8 11 4.5-1.5 8-6 8-11V5l-8-3z"/><path d="M9 12l2 2 4-4"/></svg>
</span>
<span class="brand-txt">hh X<span class="space"> </span>LevelUp</span>
</div>

<div class="welcome">
<h1>Welcome back</h1>
<p>Secure login &mdash; tokens protected.</p>
</div>

<div class="err" id="err"></div>

<form id="f">
<div class="f">
<label>Username</label>
<div class="iw">
<svg class="lft" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<input type="text" id="u" placeholder="jane.doe" autocomplete="username" required>
</div>
</div>

<div class="f">
<label>Password</label>
<div class="iw">
<svg class="lft" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
<svg class="rgt" id="eye" viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
<input type="password" id="p" placeholder="••••••••••" autocomplete="current-password" required>
</div>
</div>

<div class="remember">
<input type="checkbox" id="rm" checked>
<label for="rm">Remember me</label>
</div>

<button type="submit" class="btn" id="sb">
Login
<svg viewBox="0 0 24 24"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" y1="12" x2="3" y2="12"/></svg>
</button>
</form>

<div class="foot">New here? <a href="/plans">Create account</a></div>
</div>

<script>
const eye=document.getElementById('eye');
const pw=document.getElementById('p');
eye.addEventListener('click',()=>{
const t=pw.type==='password'?'text':'password';
pw.type=t;
eye.style.stroke=t==='text'?'#fff':'#6a6a6a';
});

document.getElementById('f').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('err');
const btn=document.getElementById('sb');
err.classList.remove('on');
btn.disabled=true;btn.firstChild.textContent='Signing in...';
const u=document.getElementById('u').value.trim();
const p=document.getElementById('p').value;
try{
const r=await fetch('/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p})});
const d=await r.json();
if(d.status==='ok')window.location.href=d.redirect||'/dashboard';
else{err.textContent=d.error||'Login Failed';err.classList.add('on')}
}catch(ex){err.textContent='Network Error';err.classList.add('on')}
btn.disabled=false;btn.firstChild.textContent='Login';
});
</script>
</body>
</html>
"""


# ==================== PLANS ====================
PLANS_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Pricing - hh X Level Up</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:radial-gradient(ellipse at top,#0a1020 0%,#000 55%);padding-bottom:60px}
.head{display:flex;align-items:center;justify-content:space-between;padding:18px 22px;border-bottom:1px solid var(--line);max-width:1400px;margin:0 auto}
.logo{display:flex;align-items:center;gap:10px;font-family:'Orbitron',sans-serif;font-size:14px;font-weight:700;letter-spacing:2px}
.logo .lm{width:36px;height:36px;background:linear-gradient(135deg,#3b82f6,#8b5cf6);border-radius:10px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:16px;box-shadow:0 0 20px rgba(59,130,246,0.35)}
.wrap{max-width:1200px;margin:0 auto;padding:44px 22px 0}
.t{text-align:center;font-family:'Orbitron',sans-serif;font-size:30px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px}
.sub{text-align:center;font-size:11px;color:var(--mut);letter-spacing:4px;text-transform:uppercase;margin-bottom:14px;font-weight:600}
.note{text-align:center;font-size:12px;color:#7a8ba0;max-width:640px;margin:0 auto 40px;line-height:1.6;padding:12px 18px;background:rgba(59,130,246,0.05);border:1px solid rgba(59,130,246,0.15);border-radius:10px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:20px}
@media(max-width:700px){.grid{grid-template-columns:1fr}}

.pc{background:var(--card);border:1.5px solid var(--line2);border-radius:20px;padding:36px 24px 24px;position:relative;transition:all 0.3s;display:flex;flex-direction:column}
.pc.blue{border-color:rgba(59,130,246,0.45)}
.pc.blue:hover{border-color:#3b82f6;box-shadow:0 0 40px rgba(59,130,246,0.25);transform:translateY(-4px)}
.pc.purple{border-color:rgba(139,92,246,0.5)}
.pc.purple:hover{border-color:#8b5cf6;box-shadow:0 0 40px rgba(139,92,246,0.3);transform:translateY(-4px)}
.pc.gold{border-color:rgba(245,158,11,0.5)}
.pc.gold:hover{border-color:#f59e0b;box-shadow:0 0 40px rgba(245,158,11,0.25);transform:translateY(-4px)}
.ribbon{position:absolute;top:-12px;right:22px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.5px;padding:6px 14px;border-radius:20px;text-transform:uppercase;box-shadow:0 4px 20px rgba(139,92,246,0.5)}
.pi{width:70px;height:70px;margin:0 auto 22px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.pc.blue .pi{background:rgba(59,130,246,0.08);border:1.5px solid rgba(59,130,246,0.35);color:#60a5fa}
.pc.purple .pi{background:rgba(139,92,246,0.08);border:1.5px solid rgba(139,92,246,0.4);color:#a78bfa}
.pc.gold .pi{background:rgba(245,158,11,0.08);border:1.5px solid rgba(245,158,11,0.4);color:#fbbf24}
.pi svg{width:30px;height:30px}
.pn{text-align:center;font-family:'Orbitron',sans-serif;font-size:24px;font-weight:700;letter-spacing:6px;margin-bottom:16px;color:#fff}
.pl{display:flex;justify-content:center;align-items:center;gap:12px;margin-bottom:8px}
.op{font-family:'Inter',sans-serif;font-size:16px;font-weight:700;color:var(--dim);text-decoration:line-through}
.deal{background:#dc2626;color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.5px;padding:3px 9px;border-radius:5px}
.pm{text-align:center;font-family:'Orbitron',sans-serif;font-size:52px;font-weight:900;letter-spacing:-1px;margin-bottom:30px;line-height:1;color:#fff}
.pm .cur{font-size:30px;font-weight:700;vertical-align:top;line-height:1;display:inline-block;margin-right:2px}
.feats{list-style:none;margin-bottom:26px;flex:1}
.feats li{display:flex;align-items:flex-start;gap:12px;padding:8px 0;font-size:14px;color:#d8d8dd;line-height:1.45;font-weight:500}
.feats li .ic{flex-shrink:0;width:18px;height:18px;display:flex;align-items:center;justify-content:center;margin-top:2px;color:#22c55e}
.feats li .ic svg{width:15px;height:15px}
.bb{width:100%;padding:15px;border-radius:12px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;border:none;cursor:pointer;transition:all 0.25s;color:#fff}
.pc.blue .bb{background:linear-gradient(135deg,#3b82f6,#2563eb);box-shadow:0 6px 24px rgba(59,130,246,0.3)}
.pc.purple .bb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);box-shadow:0 6px 24px rgba(139,92,246,0.35)}
.pc.gold .bb{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 6px 24px rgba(245,158,11,0.3);color:#000}
.an{text-align:center;font-size:11px;color:var(--dim);margin-top:12px;letter-spacing:0.5px;font-weight:500}
.flink{text-align:center;margin-top:36px;font-size:13px;color:var(--mut)}
.flink a{color:#60a5fa;text-decoration:none;font-weight:700}
</style>
</head>
<body>
<div class="head">
<div class="logo"><span class="lm">M</span><span>hh X LEVEL UP</span></div>
<a href="/login" style="color:#fff;text-decoration:none;font-size:13px;font-weight:700">Login →</a>
</div>
<div class="wrap">
<div class="t">Choose Your Plan</div>
<div class="sub">Works On All Servers</div>
<div class="note">All plans work globally across every Free Fire server &mdash; IND, BD, EUROPE, SG, TH, PH, VN, MY, ID, HK, TW and more. Price shown in USD.</div>
<div class="grid" id="grid"></div>
<div class="flink">Already Have An Account? <a href="/login">Sign In</a></div>
</div>
<script>
const SVG={
check:'__SVG_CHECK__',
bolt:'__SVG_BOLT__',
star:'__SVG_STAR__',
crown:'__SVG_CROWN__'
};
const PLANS=[
{id:'starting',name:'STARTING',style:'blue',icon:'bolt',hours:24,slots:3,price:'1',old:'2',pop:false},
{id:'basic',name:'BASIC',style:'purple',icon:'star',hours:48,slots:3,price:'2',old:'4',pop:true},
{id:'premium',name:'PREMIUM',style:'gold',icon:'crown',hours:72,slots:4,price:'2.5',old:'6',pop:false}
];
const TG='Nxt_hh_s';

function feat(p){
const d=p.hours>=24?Math.round(p.hours/24)+' Day'+(p.hours>=48?'s':''):p.hours+' Hours';
const sp=p.id==='premium'?'Fastest Leveling Speed Available':'Fast Leveling Performance';
const off=p.id==='premium'?'Runs 24/7 &mdash; No Need To Stay Online':'Runs While You Are Offline';
return[
{ic:'check',txt:'Access To The Panel For '+d},
{ic:'check',txt:sp},
{ic:'check',txt:'Run Multiple Accounts At Once'},
{ic:'check',txt:'Restart & Manage Accounts Anytime'},
{ic:'check',txt:off},
{ic:'check',txt:'Telegram Payment Support & Quick Help'},
{ic:'check',txt:p.slots+' Concurrent Account'+(p.slots>1?'s':'')}
];
}

function render(){
const g=document.getElementById('grid');
let h='';
PLANS.forEach(p=>{
let fh='';
feat(p).forEach(f=>{
fh+='<li><span class="ic">'+SVG.check+'</span><span>'+f.txt+'</span></li>';
});
h+='<div class="pc '+p.style+'">';
if(p.pop)h+='<div class="ribbon">Most Popular</div>';
h+='<div class="pi">'+SVG[p.icon]+'</div>';
h+='<div class="pn">'+p.name+'</div>';
h+='<div class="pl"><span class="op">$'+p.old+'</span><span class="deal">Deal</span></div>';
h+='<div class="pm"><span class="cur">$</span>'+p.price+'</div>';
h+='<ul class="feats">'+fh+'</ul>';
h+='<button class="bb" onclick="buy(\\''+p.id+'\\')">Buy '+p.name+'</button>';
h+='<div class="an">Instant Activation After Payment</div>';
h+='</div>';
});
g.innerHTML=h;
}

function buy(id){
const p=PLANS.find(x=>x.id===id);
let m='Hi, I Want To Buy The '+p.name+' Plan.\\n\\nPlan: $'+p.price+'\\nDuration: '+p.hours+' Hours\\nSlots: '+p.slots+'\\n\\nPlease Send Payment Details.';
window.open('https://t.me/'+TG+'?text='+encodeURIComponent(m),'_blank');
}
render();
</script>
</body>
</html>
"""

PLANS_HTML = PLANS_HTML.replace("__SVG_CHECK__", _icon("check", "#22c55e", 15).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_BOLT__", _icon("bolt_fill", "currentColor", 30).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_STAR__", _icon("star_fill", "currentColor", 30).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_CROWN__", _icon("crown_fill", "currentColor", 30).replace('"', '\\"'))


# ==================== EXPIRED ====================
EXPIRED_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Plan Expired - hh X Level Up</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{display:flex;align-items:center;justify-content:center;padding:24px;background:radial-gradient(ellipse at top,#200a0a 0%,#000 60%)}
.wrap{width:100%;max-width:460px;text-align:center}
.ic{width:84px;height:84px;border-radius:50%;background:rgba(239,68,68,0.08);border:1.5px solid var(--red);display:inline-flex;align-items:center;justify-content:center;margin-bottom:24px;color:var(--red)}
h1{font-family:'Orbitron',sans-serif;font-size:26px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px}
p{font-size:14px;color:var(--mut);line-height:1.7;margin-bottom:30px}
.br{display:flex;flex-direction:column;gap:10px;max-width:300px;margin:0 auto}
.b{display:block;padding:14px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;text-decoration:none;text-align:center;transition:all 0.2s;border:none;cursor:pointer}
.b1{background:linear-gradient(135deg,#3b82f6,#2563eb);color:#fff}
.b1:hover{box-shadow:0 8px 28px rgba(59,130,246,0.5)}
.b2{background:transparent;border:1px solid var(--line2);color:var(--mut)}
.b2:hover{border-color:var(--red);color:var(--red)}
</style>
</head>
<body>
<div class="wrap">
<div class="ic">""" + _icon("warn", "currentColor", 40) + """</div>
<h1>Plan Expired</h1>
<p>Your Plan Has Ended And All Bots Have Been Stopped.<br>To Renew, Contact @Nxt_hh_s On Telegram.</p>
<div class="br">
<a class="b b1" href="/plans">Renew Plan</a>
<a class="b b2" href="/logout">Logout</a>
</div>
</div>
</body>
</html>
"""


# ==================== DASHBOARD ====================
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
.c-stat .v.g{color:#22c55e}

/* Green + Number gain badge */
.gain-pop-green{
  display:inline-block;
  color:#22c55e;
  background:rgba(34,197,94,0.16);
  border:1px solid rgba(34,197,94,0.45);
  padding:1px 5px;
  border-radius:5px;
  font-size:10px;
  font-weight:800;
  margin-left:3px;
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

    <!-- User Meta & Quick Actions -->
    <div class="user-meta">
      <div class="mi"><span class="l">User</span><span class="v" id="ui-u">{{USERNAME}}</span></div>
      <div class="mi"><span class="l">Time</span><span class="v" id="ui-t">--</span></div>
      <div class="act">
        <button class="bs bf" id="rf" title="Refresh">__ICON_REFRESH__</button>
        <a class="bs bw" href="/plans">Buy</a>
        <a class="bs bg" href="/logout">Logout</a>
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
  const visible = getVisibleAccounts();

  if(visible.length === 0){
    grid.innerHTML = '<div class="empty-box"><p>No accounts match the "' + currentFilter.toUpperCase() + '" filter.</p></div>';
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
    html += '<input type="checkbox" class="card-chk" ' + (isSelected ? 'checked' : '') + ' onchange="toggleSelect(\'' + uid + '\', this.checked)">';
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
    html += '<div class="c-stat"><div class="l">Gained</div><div class="v g">+' + gained.toLocaleString() + (gainBadgeHtml ? ' ' + gainBadgeHtml : '') + '</div></div>';
    html += '<div class="c-stat"><div class="l">Matches</div><div class="v">' + matches + '</div></div>';
    html += '</div>';

    // Action buttons
    html += '<div class="card-actions">';
    html += '<button type="button" class="c-btn" title="Pause / Resume" onclick="singleAction(\'' + uid + '\', \'' + (isPaused ? 'resume' : 'pause') + '\')">' + (isPaused ? '▶ Run' : '⏸ Pause') + '</button>';
    html += '<button type="button" class="c-btn" title="Relogin" onclick="singleAction(\'' + uid + '\', \'relogin\')">🔄 Relogin</button>';
    html += '<button type="button" class="c-btn" title="Toggle Queue" onclick="singleAction(\'' + uid + '\', \'' + (status === 'RUNNING' ? 'move_waiting' : 'move_running') + '\')">' + (status === 'RUNNING' ? '⏳ Wait' : '▶ Slot') + '</button>';
    html += '<button type="button" class="c-btn del" title="Delete" onclick="deleteSingleAccount(\'' + uid + '\')">🗑</button>';
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
  if(st.days) document.getElementById('inp-days').value = st.days;

  // Active Slots
  if(st.active_slots) document.getElementById('inp-slots').value = st.active_slots;

  // Retry
  if(st.login_retry) document.getElementById('inp-retry').value = st.login_retry;

  // Daily Limit
  if(st.daily_limit !== undefined) document.getElementById('inp-daily-limit').value = st.daily_limit;

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
    document.getElementById('inp-exp-limit').value = st.exp_limit;
    const expHint = document.getElementById('hint-exp-limit');
    if(parseInt(st.exp_limit) > 0) expHint.textContent = 'Limit: ' + parseInt(st.exp_limit).toLocaleString() + ' EXP (Target Complete)';
    else expHint.textContent = 'No limit (accounts are never auto-deleted)';
  }

  // Level Limit
  if(st.level_limit !== undefined){
    document.getElementById('inp-level-limit').value = st.level_limit;
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
  if(s <= 0) return 'Expired';
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
    if(r.status === 401){ window.location.href = '/login'; return; }
    const d = await r.json();

    if(d.expired){ window.location.href = '/expired'; return; }

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
    document.getElementById('ui-u').textContent = d.username || 'User';
    document.getElementById('ui-t').textContent = fmtLeft(d.seconds_left || 0);

    renderCards();
  }catch(ex){
    console.error('fetchStats error:', ex);
  }
}

// Settings Handlers
function toggleDailyAutoplay(){
  cachedSettings.daily_autoplay = !cachedSettings.daily_autoplay;
  updateControlsUI(cachedSettings);
}
function adjustSlots(delta){
  const inp = document.getElementById('inp-slots');
  let val = Math.max(1, (parseInt(inp.value) || 1) + delta);
  inp.value = val;
  cachedSettings.active_slots = val;
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
    await fetch('/api/settings/save', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload)
    });
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
    await fetch('/api/account/bulk-action', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ action: act, uids: uids })
    });
    if(act === 'delete') selectedUids.clear();
    fetchStats();
  }catch(e){}
}

async function singleAction(uid, act){
  try{
    await fetch('/api/account/bulk-action', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ action: act, uids: [String(uid)] })
    });
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
    await fetch('/api/account/clear-all', {method: 'POST'});
    selectedUids.clear();
    fetchStats();
  }catch(e){}
}

// Bulk Add Modal Handlers
function openBulkAdd(){
  document.getElementById('modal-bulk-add').classList.add('on');
  document.getElementById('bulk-err').classList.remove('on');
  document.getElementById('bulk-text').value = '';
  updateBulkCount();
}
function closeBulkAdd(){
  document.getElementById('modal-bulk-add').classList.remove('on');
}
function updateBulkCount(){
  const txt = document.getElementById('bulk-text').value.trim();
  const count = txt ? txt.split('\n').filter(l => l.trim().length > 0).length : 0;
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
    const d = await r.json();
    if(d.status === 'ok'){
      closeBulkAdd();
      fetchStats();
    } else {
      err.textContent = d.error || 'Failed to add accounts';
      err.classList.add('on');
    }
  }catch(ex){
    err.textContent = 'Network error while adding accounts';
    err.classList.add('on');
  }
  btn.disabled = false;
  btn.textContent = 'Import Accounts';
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
# ==================== ADMIN LOGIN ====================
ADMIN_LOGIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Admin Access</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{display:flex;align-items:center;justify-content:center;padding:24px;background:radial-gradient(ellipse at top,#1a0a1a 0%,#000 60%)}
.wrap{width:100%;max-width:380px}
.badge{text-align:center;margin-bottom:30px}
.badge .ic{display:inline-flex;width:60px;height:60px;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.4);border-radius:14px;align-items:center;justify-content:center;margin-bottom:16px;color:var(--red)}
.badge .ic svg{width:26px;height:26px}
.badge h2{font-family:'Orbitron',sans-serif;font-size:17px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.badge p{font-size:10px;color:var(--red);margin-top:8px;letter-spacing:3px;text-transform:uppercase;opacity:0.8;font-weight:700}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:28px}
.f{margin-bottom:16px}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:7px}
.f input{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:12px 14px;color:#fff;font-size:15px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s}
.f input:focus{border-color:var(--red);box-shadow:0 0 0 3px rgba(239,68,68,0.15)}
.btn{width:100%;background:linear-gradient(135deg,#ef4444,#dc2626);color:#fff;border:none;border-radius:10px;padding:14px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;transition:all 0.2s}
.btn:hover{box-shadow:0 8px 28px rgba(239,68,68,0.45)}
.err{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);color:var(--red);padding:12px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none}
.err.on{display:block}
</style>
</head>
<body>
<div class="wrap">
<div class="badge">
<div class="ic">""" + _icon("warn", "currentColor", 26) + """</div>
<h2>Admin Access</h2>
<p>Restricted Area</p>
</div>
<div class="card">
<div id="err" class="err"></div>
<form id="f">
<div class="f"><label>Admin Username</label><input type="text" id="u" autocomplete="off" required></div>
<div class="f"><label>Admin Password</label><input type="password" id="p" autocomplete="off" required></div>
<button type="submit" class="btn">Access Panel</button>
</form>
</div>
</div>
<script>
document.getElementById('f').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('err');
err.classList.remove('on');
const u=document.getElementById('u').value.trim();
const p=document.getElementById('p').value;
try{
const r=await fetch(window.location.pathname,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p})});
const d=await r.json();
if(d.status==='ok')window.location.href=d.redirect;
else{err.textContent=d.error||'Access Denied';err.classList.add('on')}
}catch(ex){err.textContent='Network Error';err.classList.add('on')}
});
</script>
</body>
</html>
"""


# ==================== ADMIN PANEL ====================
ADMIN_PANEL_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Admin Panel - hh X Level Up</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:#000}
.top{background:rgba(0,0,0,0.95);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50}
.top-in{max-width:1400px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between}
.logo{display:flex;align-items:center;gap:10px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px}
.lm{width:30px;height:30px;background:linear-gradient(135deg,#ef4444,#b91c1c);color:#fff;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:14px}
.out{background:transparent;border:1px solid var(--line2);color:var(--mut);padding:8px 14px;border-radius:8px;font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;transition:all 0.2s}
.out:hover{border-color:var(--red);color:var(--red)}
.main{max-width:1400px;margin:0 auto;padding:28px 24px 80px}
.st{font-family:'Orbitron',sans-serif;font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:14px;display:flex;align-items:center;gap:10px}
.st::before{content:'';width:3px;height:16px;background:#fff;border-radius:2px}
.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:28px}
.grid4{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px;margin-bottom:18px}
@media(max-width:900px){.grid4{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.grid4{grid-template-columns:1fr}}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px}
.f input{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:11px 14px;color:#fff;font-size:14px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s}
.f input:focus{border-color:#3b82f6}
.btn{background:linear-gradient(135deg,#3b82f6,#2563eb);color:#fff;border:none;padding:12px 26px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;transition:all 0.2s}
.btn:hover{box-shadow:0 8px 24px rgba(59,130,246,0.4)}
.hint{font-size:11px;color:var(--mut);margin-top:10px}
.tw{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;padding:14px 16px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;color:var(--mut);letter-spacing:1.5px;text-transform:uppercase;border-bottom:1px solid var(--line2);background:var(--card2)}
td{padding:14px 16px;border-bottom:1px solid var(--line);vertical-align:middle;color:#fff}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:rgba(255,255,255,0.02)}
.mono{font-family:'JetBrains Mono',monospace;font-size:12px}
.muted{color:var(--mut)}
.badge{display:inline-block;padding:4px 10px;border-radius:6px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1px}
.ba{background:rgba(34,197,94,0.15);color:var(--green);border:1px solid rgba(34,197,94,0.3)}
.be{background:rgba(239,68,68,0.15);color:var(--red);border:1px solid rgba(239,68,68,0.3)}
.acts{display:flex;gap:6px;flex-wrap:wrap}
.mini{background:var(--card2);border:1px solid var(--line2);color:var(--mut);padding:7px 11px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1px;border-radius:6px;cursor:pointer;transition:all 0.15s}
.mini:hover{border-color:#3b82f6;color:#60a5fa}
.mini.danger:hover{border-color:var(--red);color:var(--red)}
.empty{text-align:center;padding:60px 20px;color:var(--mut);font-size:14px}
.toast{position:fixed;bottom:24px;right:24px;background:var(--card2);border:1px solid #3b82f6;color:#fff;padding:14px 20px;border-radius:10px;font-size:13px;font-weight:700;box-shadow:0 8px 32px rgba(0,0,0,0.6);opacity:0;transform:translateY(20px);transition:all 0.3s;pointer-events:none;z-index:200;max-width:360px}
.toast.on{opacity:1;transform:translateY(0)}
.toast.err{border-color:var(--red)}
</style>
</head>
<body>
<div class="top">
<div class="top-in">
<div class="logo"><span class="lm">A</span><span>hhh X LEVEL UP &mdash; ADMIN</span></div>
<a class="out" href="/admin/hh/levelup/adm-dash/logout">Logout</a>
</div>
</div>
<div class="main">
<div class="st">Create User</div>
<div class="panel">
<div class="grid4">
<div class="f"><label>Username</label><input type="text" id="nu" autocomplete="off"></div>
<div class="f"><label>Password</label><input type="text" id="np" autocomplete="off"></div>
<div class="f"><label>Slots</label><input type="number" id="ns" value="3" min="1" max="20"></div>
<div class="f"><label>Duration (Hours)</label><input type="number" id="nh" value="24" min="1" max="8760"></div>
</div>
<button class="btn" onclick="createU()">Create User</button>
<div class="hint">Timer Starts Immediately Upon Creation.</div>
</div>
<div class="st">All Users</div>
<div class="tw" id="tbl"><div class="empty">Loading...</div></div>
</div>
<div class="toast" id="toast"></div>
<script>
function esc(s){if(s==null)return'';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}
function toast(msg,err){const t=document.getElementById('toast');t.textContent=msg;t.classList.toggle('err',!!err);t.classList.add('on');setTimeout(()=>t.classList.remove('on'),2600)}
function fmtLeft(exp){const now=Math.floor(Date.now()/1000);const s=exp-now;if(s<=0)return{t:'Expired',e:true};const h=Math.floor(s/3600);const m=Math.floor((s%3600)/60);return{t:h+'h '+m+'m',e:false}}
function fmtDate(ts){return new Date(ts*1000).toLocaleString()}
async function createU(){
const u=document.getElementById('nu').value.trim();
const p=document.getElementById('np').value.trim();
const s=parseInt(document.getElementById('ns').value);
const h=parseInt(document.getElementById('nh').value);
if(!u||!p){toast('Username And Password Required',true);return}
if(s<1||s>20){toast('Slots Must Be 1-20',true);return}
if(h<1||h>8760){toast('Hours Must Be 1-8760',true);return}
try{
const r=await fetch('/api/admin/create-user',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p,slots:s,hours:h})});
const d=await r.json();
if(d.status==='ok'){toast('User Created: '+u);document.getElementById('nu').value='';document.getElementById('np').value='';loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function loadU(){
try{
const r=await fetch('/api/admin/list-users');
const d=await r.json();
if(d.status!=='ok')return;
const users=d.users||[];
const w=document.getElementById('tbl');
if(users.length===0){w.innerHTML='<div class="empty">No Users Yet</div>';return}
let h='<table><thead><tr>';
h+='<th>Username</th><th>Slots</th><th>Used</th><th>Expires</th><th>Created</th><th>Actions</th>';
h+='</tr></thead><tbody>';
users.forEach(u=>{
const e=fmtLeft(u.expires_at);
const b=e.e?'<span class="badge be">Expired</span>':'<span class="badge ba">'+e.t+'</span>';
h+='<tr>';
h+='<td class="mono">'+esc(u.username)+'</td>';
h+='<td class="mono">'+u.slots+'</td>';
h+='<td class="mono muted">'+(u.used_slots||0)+'</td>';
h+='<td>'+b+'</td>';
h+='<td class="muted">'+fmtDate(u.created_at)+'</td>';
h+='<td><div class="acts">';
h+='<button class="mini" onclick="ext(\\''+esc(u.username)+'\\',24)">+24H</button>';
h+='<button class="mini" onclick="slot(\\''+esc(u.username)+'\\',1)">+1 Slot</button>';
h+='<button class="mini danger" onclick="delU(\\''+esc(u.username)+'\\')">Delete</button>';
h+='</div></td>';
h+='</tr>'
});
h+='</tbody></table>';
w.innerHTML=h
}catch(e){}
}
async function ext(u,h){
try{
const r=await fetch('/api/admin/extend-time',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,hours:h})});
const d=await r.json();
if(d.status==='ok'){toast('Extended '+u+' By '+h+'h');loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function slot(u,c){
try{
const r=await fetch('/api/admin/add-slot',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,count:c})});
const d=await r.json();
if(d.status==='ok'){toast('Added '+c+' Slot To '+u);loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function delU(u){
if(!confirm('Delete User '+u+'? This Wipes All Their Data.'))return;
try{
const r=await fetch('/api/admin/delete-user',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u})});
const d=await r.json();
if(d.status==='ok'){toast('Deleted '+u);loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
loadU();
setInterval(loadU,5000);
</script>
</body>
</html>
"""


ALL_TEMPLATES = {
    "home": HOME_HTML,
    "login": LOGIN_HTML,
    "plans": PLANS_HTML,
    "dashboard": DASHBOARD_HTML,
    "expired": EXPIRED_HTML,
    "admin_login": ADMIN_LOGIN_HTML,
    "admin_panel": ADMIN_PANEL_HTML,
}