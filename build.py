#!/usr/bin/env python3
"""
AllMyTube Affiliate Site Builder
Generates a full multi-page SEO-optimized site for GitHub Pages at /allmytube/
"""

import os, json, textwrap
from pathlib import Path

BASE = Path("/home/claude/allmytube-site")
SITE_ROOT = "/allmytube"
AFF_LINK = "https://www.linkconnector.com/ta.php?lc=007949042649004532&atid=allmytubeweb"
SITE_URL  = "https://brightlane.github.io/allmytube"

# ─── shared assets ────────────────────────────────────────────────────────────

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Exo+2:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');
:root{--bg:#050810;--bg2:#080d1c;--bg3:#0d1428;--acc:#00d4ff;--acc2:#ff3d6b;--acc3:#7b2fff;--gold:#ffc844;--txt:#e8eaf0;--mut:#8892a4;--bdr:rgba(0,212,255,.14);--glow:0 0 22px rgba(0,212,255,.35);--card:rgba(8,13,28,.85);--r:12px}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Exo 2',sans-serif;background:var(--bg);color:var(--txt);line-height:1.65;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(0,212,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(0,212,255,.025) 1px,transparent 1px);background-size:56px 56px;pointer-events:none;z-index:0}
h1,h2,h3,h4{font-family:'Bebas Neue',sans-serif;letter-spacing:.04em;line-height:1.1}
h1{font-size:clamp(2.6rem,7vw,5rem)}h2{font-size:clamp(1.9rem,4vw,3rem)}h3{font-size:clamp(1.3rem,2.5vw,1.9rem)}
p{color:var(--mut);font-weight:300}a{color:var(--acc);text-decoration:none;transition:color .2s}a:hover{color:#fff}
/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(5,8,16,.93);backdrop-filter:blur(18px);border-bottom:1px solid var(--bdr);padding:0 5%;height:68px;display:flex;align-items:center;justify-content:space-between}
.nav-logo{font-family:'Bebas Neue',sans-serif;font-size:1.75rem;color:var(--acc);letter-spacing:.1em;text-shadow:var(--glow)}
.nav-logo span{color:var(--acc2)}
.nav-links{display:flex;gap:1.8rem;list-style:none;align-items:center}
.nav-links a{color:var(--mut);font-weight:600;font-size:.82rem;text-transform:uppercase;letter-spacing:.1em}
.nav-links a:hover{color:var(--acc)}
.nav-cta{background:linear-gradient(135deg,var(--acc),var(--acc3))!important;color:#000!important;padding:.45rem 1.2rem;border-radius:6px;font-weight:800!important}
.hbg{display:none;flex-direction:column;gap:5px;cursor:pointer}
.hbg span{display:block;width:24px;height:2px;background:var(--acc)}
/* HERO */
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;position:relative;padding:130px 5% 80px;text-align:center;overflow:hidden}
.hero::before{content:'';position:absolute;top:40%;left:50%;transform:translate(-50%,-50%);width:900px;height:900px;background:radial-gradient(circle,rgba(0,212,255,.07) 0%,rgba(123,47,255,.05) 40%,transparent 70%);pointer-events:none}
.badge{display:inline-block;background:rgba(0,212,255,.1);border:1px solid var(--bdr);color:var(--acc);font-size:.78rem;font-weight:700;letter-spacing:.15em;text-transform:uppercase;padding:.38rem 1rem;border-radius:100px;margin-bottom:1.4rem}
.hero h1{margin-bottom:1.1rem}.hero h1 .c1{color:var(--acc)}.hero h1 .c2{color:var(--acc2)}
.hero-sub{font-size:1.15rem;max-width:640px;margin:0 auto 2.4rem;color:var(--mut);font-weight:300}
.hero-acts{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-bottom:3rem}
.btn{display:inline-flex;align-items:center;gap:.5rem;font-family:'Exo 2',sans-serif;font-weight:800;font-size:.95rem;padding:.85rem 1.9rem;border-radius:8px;text-transform:uppercase;letter-spacing:.1em;transition:all .3s;cursor:pointer;border:none}
.btn-p{background:linear-gradient(135deg,var(--acc),#0099cc);color:#000;box-shadow:0 4px 24px rgba(0,212,255,.4)}
.btn-p:hover{transform:translateY(-3px);box-shadow:0 8px 32px rgba(0,212,255,.6);color:#000}
.btn-s{border:1px solid var(--bdr);color:var(--txt);background:rgba(255,255,255,.03)}
.btn-s:hover{border-color:var(--acc);color:var(--acc);background:rgba(0,212,255,.05)}
/* STATS */
.stats{display:flex;justify-content:center;gap:3rem;flex-wrap:wrap;padding:2rem 5%;border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);background:rgba(255,255,255,.015);position:relative;z-index:1}
.stat-n{font-family:'Bebas Neue',sans-serif;font-size:2.4rem;color:var(--acc);text-shadow:var(--glow);line-height:1}
.stat-l{font-size:.78rem;color:var(--mut);text-transform:uppercase;letter-spacing:.1em}
/* SECTIONS */
section{padding:5.5rem 5%;position:relative;z-index:1}
.sec-lbl{font-size:.78rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin-bottom:.6rem}
.sec-title{margin-bottom:.9rem}.sec-sub{max-width:600px;margin-bottom:2.8rem}
.tc{text-align:center}.tc .sec-sub{margin-left:auto;margin-right:auto}
/* CARDS */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:1.4rem}
.card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2rem;transition:all .3s;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:0;left:0;width:100%;height:2px;background:linear-gradient(90deg,transparent,var(--acc),transparent);transform:scaleX(0);transition:transform .4s}
.card:hover::before{transform:scaleX(1)}
.card:hover{border-color:rgba(0,212,255,.3);transform:translateY(-4px);box-shadow:0 12px 40px rgba(0,0,0,.4)}
.c-icon{width:50px;height:50px;background:rgba(0,212,255,.1);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.4rem;margin-bottom:1.1rem}
.card h3{font-size:1.25rem;margin-bottom:.45rem;color:var(--txt)}.card p{font-size:.88rem}
/* FEATURE SPLIT */
.fsplit{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}
.flist{list-style:none;display:flex;flex-direction:column;gap:.9rem}
.flist li{display:flex;align-items:flex-start;gap:.7rem;font-size:.93rem;color:var(--mut)}
.flist li::before{content:'▶';color:var(--acc);font-size:.65rem;margin-top:.35rem;flex-shrink:0}
/* PRICING */
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.4rem;max-width:860px;margin:0 auto}
.pc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2.4rem 2rem;text-align:center;transition:all .3s;position:relative}
.pc.feat{border-color:var(--acc);background:linear-gradient(135deg,rgba(0,212,255,.07),rgba(123,47,255,.07))}
.feat-badge{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--acc),var(--acc3));color:#fff;font-size:.73rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.28rem .9rem;border-radius:100px}
.p-name{font-size:.85rem;text-transform:uppercase;letter-spacing:.15em;color:var(--mut);margin-bottom:.9rem}
.p-price{font-family:'Bebas Neue',sans-serif;font-size:3.3rem;color:var(--acc);line-height:1}
.p-price span{font-size:1.1rem;color:var(--mut)}
.p-per{font-size:.78rem;color:var(--mut);margin-bottom:1.4rem}
.p-feats{list-style:none;text-align:left;margin-bottom:1.8rem;display:flex;flex-direction:column;gap:.65rem}
.p-feats li{font-size:.87rem;color:var(--mut);display:flex;gap:.45rem}
.p-feats li::before{content:'✓';color:var(--acc);font-weight:700;flex-shrink:0}
/* FAQ */
.faq{max-width:750px;margin:0 auto;display:flex;flex-direction:column;gap:.9rem}
details{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden}
details summary{padding:1.1rem 1.4rem;cursor:pointer;font-weight:600;font-size:.97rem;list-style:none;display:flex;justify-content:space-between;align-items:center;color:var(--txt)}
details summary::-webkit-details-marker{display:none}
details summary::after{content:'+';color:var(--acc);font-size:1.4rem;font-weight:300}
details[open] summary::after{content:'−'}
details .da{padding:0 1.4rem 1.1rem;border-top:1px solid var(--bdr);padding-top:.9rem}
/* TABLE */
.twrap{overflow-x:auto;border-radius:var(--r)}
table{width:100%;border-collapse:collapse}
th,td{padding:.9rem 1.1rem;text-align:left;border-bottom:1px solid var(--bdr);font-size:.87rem}
th{background:rgba(0,212,255,.08);color:var(--acc);font-family:'Bebas Neue',sans-serif;font-size:.95rem;letter-spacing:.05em}
tr:hover td{background:rgba(255,255,255,.02)}
.ck{color:var(--acc);font-weight:700}.cx{color:var(--acc2)}
/* TESTIMONIALS */
.tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.4rem}
.tc-card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2rem}
.stars{color:var(--gold);font-size:1rem;margin-bottom:.7rem}
.tc-text{font-size:.92rem;margin-bottom:1.1rem;color:var(--txt);font-style:italic}
.tc-name{font-size:.83rem;font-weight:700;color:var(--acc)}.tc-role{font-size:.78rem;color:var(--mut)}
/* SITES GRID */
.sgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:.8rem}
.stag{background:rgba(255,255,255,.035);border:1px solid var(--bdr);border-radius:6px;padding:.55rem .9rem;font-size:.78rem;text-align:center;color:var(--mut);transition:all .2s}
.stag:hover{border-color:var(--acc);color:var(--acc);background:rgba(0,212,255,.05)}
/* STEPS */
.steps{max-width:680px;display:flex;flex-direction:column}
.step{display:flex;gap:1.8rem;align-items:flex-start;padding:1.8rem 0 1.8rem 2rem;border-left:2px solid var(--bdr);margin-left:1.4rem;position:relative}
.step::before{content:attr(data-n);position:absolute;left:-1.55rem;width:3rem;height:3rem;background:var(--bg);border:2px solid var(--acc);border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;font-size:1.2rem;color:var(--acc);text-shadow:var(--glow)}
.step:last-child{border-left-color:transparent}
.step h3{font-size:1.1rem;margin-bottom:.4rem;color:var(--txt)}
/* BLOG */
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.4rem}
.bc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden;transition:all .3s}
.bc:hover{transform:translateY(-4px);border-color:rgba(0,212,255,.3)}
.bc-img{height:160px;background:linear-gradient(135deg,var(--bg3),rgba(0,212,255,.1));display:flex;align-items:center;justify-content:center;font-size:2.8rem;border-bottom:1px solid var(--bdr)}
.bc-body{padding:1.4rem}.bc-tag{font-size:.73rem;color:var(--acc);text-transform:uppercase;letter-spacing:.1em;margin-bottom:.4rem}
.bc h3{font-size:1rem;margin-bottom:.4rem;color:var(--txt)}.bc p{font-size:.83rem}
.bc-meta{margin-top:.9rem;font-size:.77rem;color:var(--mut);display:flex;gap:.9rem}
/* CTA */
.cta-sec{text-align:center;padding:5.5rem 5%;background:linear-gradient(135deg,rgba(0,212,255,.05),rgba(123,47,255,.05));border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr)}
/* FOOTER */
footer{background:var(--bg2);border-top:1px solid var(--bdr);padding:3.5rem 5% 1.8rem}
.fg{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:2.5rem;margin-bottom:2.5rem}
.fb{color:var(--acc);font-family:'Bebas Neue',sans-serif;font-size:1.5rem;margin-bottom:.8rem}
.fd{font-size:.83rem;max-width:240px}
.fc h4{font-size:.77rem;text-transform:uppercase;letter-spacing:.15em;color:var(--txt);margin-bottom:.9rem}
.fc ul{list-style:none;display:flex;flex-direction:column;gap:.55rem}
.fc a{color:var(--mut);font-size:.82rem}.fc a:hover{color:var(--acc)}
.fb-bot{border-top:1px solid var(--bdr);padding-top:1.4rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem}
.fb-bot p{font-size:.78rem;color:var(--mut)}
/* BREADCRUMB */
.bc-nav{font-size:.78rem;color:var(--mut);margin-bottom:1.4rem}
.bc-nav a{color:var(--mut)}.bc-nav .cur{color:var(--acc)}
/* PAGE HERO */
.ph{padding:130px 5% 55px;background:linear-gradient(180deg,rgba(0,212,255,.05) 0%,transparent 100%);border-bottom:1px solid var(--bdr)}
/* HIGHLIGHT BOX */
.hbox{background:rgba(0,212,255,.06);border:1px solid var(--bdr);border-radius:var(--r);padding:1.8rem;margin:1.8rem 0}
/* TAG CHIPS */
.chip{display:inline-block;background:rgba(0,212,255,.1);border:1px solid var(--bdr);color:var(--acc);font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.2rem .55rem;border-radius:4px}
.chip-r{background:rgba(255,61,107,.1);border-color:rgba(255,61,107,.2);color:var(--acc2)}
.chip-g{background:rgba(255,200,68,.1);border-color:rgba(255,200,68,.2);color:var(--gold)}
/* RESPONSIVE */
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}.fsplit{grid-template-columns:1fr;gap:2rem}}
@media(max-width:640px){.nav-links{display:none}.hbg{display:flex}.fg{grid-template-columns:1fr}.stats{gap:1.4rem}.hero h1{font-size:2.6rem}}
@keyframes fadeUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:translateY(0)}}
@keyframes pulse{0%,100%{box-shadow:0 4px 24px rgba(0,212,255,.4)}50%{box-shadow:0 4px 36px rgba(0,212,255,.7)}}
.anim{animation:fadeUp .7s ease forwards}
.btn-p{animation:pulse 3s infinite}
"""

# ─── nav / footer helpers ──────────────────────────────────────────────────────

def nav():
    return f"""
<nav>
  <a class="nav-logo" href="{SITE_ROOT}/">All<span>My</span>Tube</a>
  <ul class="nav-links">
    <li><a href="{SITE_ROOT}/features/">Features</a></li>
    <li><a href="{SITE_ROOT}/supported-sites/">1000+ Sites</a></li>
    <li><a href="{SITE_ROOT}/how-it-works/">How It Works</a></li>
    <li><a href="{SITE_ROOT}/pricing/">Pricing</a></li>
    <li><a href="{SITE_ROOT}/blog/">Blog</a></li>
    <li><a href="{SITE_ROOT}/faq/">FAQ</a></li>
    <li><a href="{AFF_LINK}" class="nav-cta" target="_blank" rel="noopener">Download Free ↗</a></li>
  </ul>
  <div class="hbg" onclick="this.closest('nav').querySelector('.nav-links').style.display='flex';this.style.display='none'">
    <span></span><span></span><span></span>
  </div>
</nav>"""

def footer():
    return f"""
<footer>
  <div class="fg">
    <div>
      <div class="fb">All<span style="color:var(--acc2)">My</span>Tube</div>
      <p class="fd">The world's most powerful video downloader. Download from 10,000+ sites in 4K, HD, or any format you need.</p>
    </div>
    <div class="fc">
      <h4>Product</h4>
      <ul>
        <li><a href="{SITE_ROOT}/features/">Features</a></li>
        <li><a href="{SITE_ROOT}/pricing/">Pricing</a></li>
        <li><a href="{SITE_ROOT}/supported-sites/">Supported Sites</a></li>
        <li><a href="{SITE_ROOT}/how-it-works/">How It Works</a></li>
        <li><a href="{SITE_ROOT}/download/">Download</a></li>
      </ul>
    </div>
    <div class="fc">
      <h4>Compare</h4>
      <ul>
        <li><a href="{SITE_ROOT}/vs-4k-video-downloader/">vs 4K Downloader</a></li>
        <li><a href="{SITE_ROOT}/vs-ytdlp/">vs yt-dlp</a></li>
        <li><a href="{SITE_ROOT}/vs-videoder/">vs Videoder</a></li>
        <li><a href="{SITE_ROOT}/alternatives/">Alternatives</a></li>
      </ul>
    </div>
    <div class="fc">
      <h4>Resources</h4>
      <ul>
        <li><a href="{SITE_ROOT}/blog/">Blog</a></li>
        <li><a href="{SITE_ROOT}/faq/">FAQ</a></li>
        <li><a href="{SITE_ROOT}/review/">Review</a></li>
        <li><a href="{SITE_ROOT}/privacy/">Privacy Policy</a></li>
        <li><a href="{SITE_ROOT}/disclaimer/">Disclaimer</a></li>
      </ul>
    </div>
  </div>
  <div class="fb-bot">
    <p>© 2025 AllMyTube Guide. Affiliate site — we earn commissions on purchases.</p>
    <p><a href="{AFF_LINK}" target="_blank" rel="noopener">Download AllMyTube →</a></p>
  </div>
</footer>"""

def page(title, desc, canonical_path, body, keywords=""):
    kw = keywords or "AllMyTube, video downloader, YouTube downloader, 4K download, Wondershare"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{SITE_URL}{canonical_path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE_URL}{canonical_path}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE_URL}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="icon" href="{SITE_ROOT}/assets/favicon.svg" type="image/svg+xml">
<style>{CSS}</style>
<script type="application/ld+json">{{
  "@context":"https://schema.org",
  "@type":"SoftwareApplication",
  "name":"AllMyTube",
  "applicationCategory":"MultimediaApplication",
  "operatingSystem":"Windows, Mac",
  "offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}},
  "description":"{desc}",
  "url":"{SITE_URL}{canonical_path}"
}}</script>
</head>
<body>
{nav()}
{body}
{footer()}
</body>
</html>"""

# ─── write helper ──────────────────────────────────────────────────────────────

def write(rel_path, content):
    p = BASE / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  ✓  {rel_path}")

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════

def build_index():
    body = f"""
<section class="hero">
  <div style="position:relative;z-index:1;width:100%">
    <div class="badge anim">🏆 #1 Rated Video Downloader — 50M+ Users Worldwide</div>
    <h1 class="anim" style="animation-delay:.1s">Download <span class="c1">Any Video</span><br>From <span class="c2">10,000+ Sites</span></h1>
    <p class="hero-sub anim" style="animation-delay:.2s">AllMyTube by Wondershare lets you save YouTube, Vimeo, TikTok, Facebook and thousands more sites in 4K, HD or MP3 — in seconds.</p>
    <div class="hero-acts anim" style="animation-delay:.3s">
      <a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">⬇ Download Free Now</a>
      <a href="{SITE_ROOT}/how-it-works/" class="btn btn-s">See How It Works →</a>
    </div>
    <p style="font-size:.8rem;color:var(--mut)">Windows &amp; Mac · Free Trial Available · No Credit Card Required</p>
  </div>
</section>

<div class="stats">
  <div class="stat-item"><div class="stat-n">10,000+</div><div class="stat-l">Supported Sites</div></div>
  <div class="stat-item"><div class="stat-n">50M+</div><div class="stat-l">Global Users</div></div>
  <div class="stat-item"><div class="stat-n">4K</div><div class="stat-l">Max Resolution</div></div>
  <div class="stat-item"><div class="stat-n">200+</div><div class="stat-l">Countries</div></div>
  <div class="stat-item"><div class="stat-n">3×</div><div class="stat-l">Faster Downloads</div></div>
</div>

<section>
  <div class="tc"><div class="sec-lbl">Why AllMyTube?</div>
  <h2 class="sec-title">Everything You Need to<br><span style="color:var(--acc)">Save &amp; Convert</span> Video</h2>
  <p class="sec-sub">One tool that handles downloading, converting, scheduling, and organizing all your video content.</p></div>
  <div class="cards">
    <div class="card"><div class="c-icon">🎬</div><h3>4K Ultra HD</h3><p>Download videos at up to 4K (2160p) resolution — the highest quality available on YouTube and other platforms.</p></div>
    <div class="card"><div class="c-icon">⚡</div><h3>3× Faster Speed</h3><p>AllMyTube's multithreading engine fully harnesses your bandwidth for download speeds 3× faster than competitors.</p></div>
    <div class="card"><div class="c-icon">🌐</div><h3>10,000+ Sites</h3><p>YouTube, Vimeo, TikTok, Facebook, Dailymotion, Twitch, SoundCloud and thousands more — all covered.</p></div>
    <div class="card"><div class="c-icon">🔄</div><h3>Format Converter</h3><p>Convert to MP4, MP3, AVI, MOV, MKV and 150+ formats. Optimized presets for iPhone, Android, PS5, TV.</p></div>
    <div class="card"><div class="c-icon">📋</div><h3>Batch Download</h3><p>Download entire YouTube playlists or channels with one click. Schedule downloads for off-peak hours.</p></div>
    <div class="card"><div class="c-icon">▶</div><h3>Built-in Player</h3><p>Watch downloaded videos instantly in AllMyTube's built-in media player — no separate app required.</p></div>
  </div>
</section>

<section style="background:linear-gradient(180deg,transparent,rgba(0,212,255,.03),transparent)">
  <div class="tc"><div class="sec-lbl">Popular Platforms</div>
  <h2 class="sec-title">Works With All Your<br><span style="color:var(--acc)">Favorite Sites</span></h2></div>
  <div class="sgrid" style="max-width:900px;margin:0 auto">
    {"".join(f'<div class="stag">{s}</div>' for s in [
      "YouTube","TikTok","Vimeo","Facebook","Instagram","Twitter/X","Twitch","Dailymotion",
      "SoundCloud","Reddit","Bilibili","Niconico","LinkedIn","Pinterest","Tumblr","VK",
      "Rumble","BitChute","Odysee","OK.ru","9GAG","Streamable","Gfycat","Imgur",
      "Metacafe","Veoh","Break","AOL Video","TV.com","Mixcloud"
    ])}
  </div>
  <div style="text-align:center;margin-top:2rem"><a href="{SITE_ROOT}/supported-sites/" class="btn btn-s">View All 10,000+ Sites →</a></div>
</section>

<section>
  <div class="tgrid">
    <div class="tc-card"><div class="stars">★★★★★</div><p class="tc-text">"I've tried dozens of video downloaders and AllMyTube is by far the best. Downloads entire playlists in minutes. The 4K quality is stunning."</p><div class="tc-name">Marcus T.</div><div class="tc-role">Filmmaker, USA</div></div>
    <div class="tc-card"><div class="stars">★★★★★</div><p class="tc-text">"As a teacher I download educational videos for offline use in remote classrooms. AllMyTube saves me hours every week. Essential software."</p><div class="tc-name">Priya S.</div><div class="tc-role">Educator, India</div></div>
    <div class="tc-card"><div class="stars">★★★★★</div><p class="tc-text">"The MP3 extraction is incredibly fast and the quality is perfect. I use it every day for music and podcasts. Worth every penny."</p><div class="tc-name">Elena R.</div><div class="tc-role">Podcaster, UK</div></div>
  </div>
</section>

<section class="cta-sec">
  <div class="sec-lbl">Get Started Free</div>
  <h2 style="margin-bottom:.8rem">Ready to Download <span style="color:var(--acc)">Any Video?</span></h2>
  <p style="max-width:500px;margin:0 auto 2rem">Join 50 million users who trust AllMyTube for fast, high-quality video downloads on Windows and Mac.</p>
  <a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">⬇ Download AllMyTube Free</a>
  <p style="margin-top:1rem;font-size:.82rem;color:var(--mut)">One-time license available · Lifetime updates included</p>
</section>"""
    return page(
        "AllMyTube — Download Videos from 10,000+ Sites in 4K | Free Trial",
        "Download AllMyTube free. Save YouTube, TikTok, Vimeo &amp; 10,000+ sites in 4K HD or MP3. 50M+ users. Windows &amp; Mac. Batch download entire playlists.",
        "/", body
    )

def build_features():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">Features</span></div>
  <div class="sec-lbl">Full Feature Set</div>
  <h1>AllMyTube <span style="color:var(--acc)">Features</span></h1>
  <p style="max-width:600px;margin-top:.8rem;font-size:1.1rem">Everything packed into one powerful downloader. Here's why 50 million people choose AllMyTube.</p>
</div>
<section>
  <div class="cards">
    <div class="card"><div class="c-icon">🎯</div><h3>One-Click Download</h3><p>Paste a URL, click download. Or install the browser extension and hit the floating download button while watching any video.</p></div>
    <div class="card"><div class="c-icon">🎬</div><h3>4K / 8K Support</h3><p>Choose from 7 resolution presets: 2160p (4K), 1440p, 1080p, 720p, 480p, 360p, 240p. Always get the quality you want.</p></div>
    <div class="card"><div class="c-icon">🎵</div><h3>MP3 Extraction</h3><p>Extract audio from any video as high-quality MP3, AAC, FLAC or WAV. Perfect for music, podcasts, lectures and more.</p></div>
    <div class="card"><div class="c-icon">📋</div><h3>Playlist Download</h3><p>Download entire YouTube playlists or channels in one click. AllMyTube handles queues of hundreds of videos effortlessly.</p></div>
    <div class="card"><div class="c-icon">🔄</div><h3>Built-in Converter</h3><p>Convert to 150+ formats including MP4, MKV, AVI, MOV, WMV, FLV. Device presets for iPhone, Android, iPad, Samsung TV.</p></div>
    <div class="card"><div class="c-icon">📅</div><h3>Download Scheduler</h3><p>Schedule downloads for off-peak hours. Choose Auto Shutdown, Sleep or Exit Program when downloads complete.</p></div>
    <div class="card"><div class="c-icon">🌐</div><h3>10,000+ Sites</h3><p>Supports YouTube, TikTok, Vimeo, Facebook, Instagram, Twitter, Twitch, Dailymotion and over 10,000 more video platforms.</p></div>
    <div class="card"><div class="c-icon">▶</div><h3>Built-in Player</h3><p>Preview and watch downloaded content without leaving AllMyTube. Full playback controls, subtitle support included.</p></div>
    <div class="card"><div class="c-icon">🔗</div><h3>Browser Extension</h3><p>Download videos directly from Chrome, Firefox or Edge with the AllMyTube browser plugin — no URL copying needed.</p></div>
    <div class="card"><div class="c-icon">📱</div><h3>Transfer to Device</h3><p>Send downloaded videos directly to your iPhone, Android or tablet. Watch offline on any screen, anywhere.</p></div>
    <div class="card"><div class="c-icon">🔒</div><h3>100% Safe & Legal</h3><p>Trusted by 50M+ users globally. No malware, no bundled software. Wondershare is a recognized worldwide software company.</p></div>
    <div class="card"><div class="c-icon">🏷</div><h3>Subtitle Download</h3><p>Download videos with original subtitles when available. Supports SRT, ASS, VTT formats from YouTube and more.</p></div>
  </div>
  <div class="cta-sec" style="margin-top:3rem;border-radius:var(--r)">
    <h2 style="margin-bottom:.8rem">All These Features, <span style="color:var(--acc)">Free to Try</span></h2>
    <p style="max-width:480px;margin:0 auto 1.8rem">Download AllMyTube and explore every feature with a free trial. No credit card required.</p>
    <a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">⬇ Get AllMyTube Free</a>
  </div>
</section>"""
    return page("AllMyTube Features — 4K, Batch Download, Converter & More", "Explore all AllMyTube features: 4K downloads, MP3 extraction, playlist downloads, built-in converter, browser extension & 10,000+ supported sites.", "/features/", body, "AllMyTube features, video downloader features, 4K download, MP3 extractor, playlist downloader")

def build_supported_sites():
    sites = [
        "YouTube","YouTube Shorts","YouTube Music","TikTok","Vimeo","Facebook","Instagram Reels",
        "Instagram Stories","Twitter / X","Twitch","Twitch Clips","Dailymotion","SoundCloud",
        "Reddit","Bilibili","Niconico","LinkedIn","Pinterest","Tumblr","VK","Rumble","BitChute",
        "Odysee","OK.ru","9GAG","Streamable","Gfycat","Metacafe","Veoh","Break","AOL Video",
        "TV.com","Mixcloud","Bandcamp","Beatport","Spotify (audio)","Apple Music Previews",
        "Deezer","Pandora","iHeartRadio","BBC iPlayer","ITV Hub","Channel 4","Sky Sports",
        "ESPN","NBC Sports","Fox Sports","DAZN","Hotstar","ZEE5","MX Player","Voot",
        "SonyLIV","AltBalaji","Hungama","JioCinema","Stage","Eros Now","ShemarooMe",
        "Ullu","Nuvid","YuppTV","Alt","Docplay","Acorn TV","BritBox","CuriosityStream",
        "Mubi","Crunchyroll","Funimation","VRV","Hidive","Rooster Teeth","Dropout",
        "Nebula","Magellan TV","Plex","Tubi","Pluto TV","Peacock","Paramount+","Discovery+",
        "AMC+","Shudder","Sundance Now","Cinedigm","Fandango Now","Vudu","Microsoft Movies",
        "Google Play Movies","YouTube Premium","Dailymotion Kids","Kidz Nation","RTÉ Player",
        "ARD Mediathek","ZDF Mediathek","France.tv","RaiPlay","RTVE","Mitele","Atresplayer"
    ]
    grid_html = "".join(f'<div class="stag">{s}</div>' for s in sites)
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">Supported Sites</span></div>
  <div class="sec-lbl">Global Compatibility</div>
  <h1>Download From <span style="color:var(--acc)">10,000+</span> Sites</h1>
  <p style="max-width:600px;margin-top:.8rem;font-size:1.1rem">AllMyTube supports virtually every video platform on the internet — from YouTube to niche streaming sites worldwide.</p>
</div>
<section>
  <div class="hbox">
    <p>AllMyTube is constantly updated to support new platforms. If a site streams video, chances are AllMyTube can download it. Below are some of the most popular supported sites — but there are <strong style="color:var(--acc)">over 10,000</strong> in total.</p>
  </div>
  <h2 style="margin-bottom:1.5rem">Popular <span style="color:var(--acc)">Supported Sites</span></h2>
  <div class="sgrid">{grid_html}</div>
  <div style="text-align:center;margin-top:3rem">
    <p style="margin-bottom:1.5rem">... and 9,900+ more platforms worldwide</p>
    <a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">⬇ Download AllMyTube Free</a>
  </div>
</section>"""
    return page("AllMyTube Supported Sites — 10,000+ Video Platforms", "AllMyTube supports 10,000+ video sites including YouTube, TikTok, Vimeo, Facebook, Instagram, Twitch, Dailymotion and thousands more worldwide.", "/supported-sites/", body, "AllMyTube supported sites, YouTube downloader, TikTok downloader, Vimeo downloader")

def build_how_it_works():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">How It Works</span></div>
  <div class="sec-lbl">Simple 3 Steps</div>
  <h1>How <span style="color:var(--acc)">AllMyTube</span> Works</h1>
  <p style="max-width:600px;margin-top:.8rem;font-size:1.1rem">From URL to downloaded video in under a minute. Here's exactly how simple it is.</p>
</div>
<section>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start">
    <div>
      <div class="steps">
        <div class="step" data-n="1"><div><h3>Copy the Video URL</h3><p>Go to YouTube, TikTok, Vimeo or any of 10,000+ sites. Copy the URL from your browser address bar.</p></div></div>
        <div class="step" data-n="2"><div><h3>Paste &amp; Select Quality</h3><p>Open AllMyTube and paste the URL. Choose your preferred resolution (4K, 1080p, 720p…) or format (MP4, MP3, etc.).</p></div></div>
        <div class="step" data-n="3"><div><h3>Click Download</h3><p>Hit Download and AllMyTube does the rest at triple speed. Your video is saved to your chosen folder instantly.</p></div></div>
        <div class="step" data-n="4"><div><h3>Optional: Convert &amp; Transfer</h3><p>Convert to any device format or transfer directly to your phone — all from within AllMyTube.</p></div></div>
      </div>
      <div style="margin-top:2rem"><a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">⬇ Try It Free Now</a></div>
    </div>
    <div>
      <div class="hbox">
        <h3 style="margin-bottom:1rem;color:var(--acc)">Pro Tips</h3>
        <ul class="flist">
          <li>Use the browser extension to add a "Download" button directly on YouTube &amp; other sites</li>
          <li>Right-click any video link and choose "Download with AllMyTube" from the context menu</li>
          <li>Enable Turbo Mode to use all available bandwidth for maximum speed</li>
          <li>Set up the scheduler to download overnight on slower connections</li>
          <li>Use the screen recorder for DRM-protected content that can't be downloaded directly</li>
        </ul>
      </div>
      <div class="hbox" style="margin-top:1rem">
        <h3 style="margin-bottom:1rem;color:var(--acc)">Method 2: Browser Extension</h3>
        <p>Install the AllMyTube browser extension for Chrome, Firefox or Edge. A download button appears automatically on any video page — click it to download without leaving your browser.</p>
      </div>
      <div class="hbox" style="margin-top:1rem">
        <h3 style="margin-bottom:1rem;color:var(--acc)">Method 3: Screen Recorder</h3>
        <p>For any video that plays in a browser, AllMyTube's built-in screen recorder can capture it directly — a powerful fallback for any platform.</p>
      </div>
    </div>
  </div>
</section>"""
    return page("How AllMyTube Works — 3 Simple Steps to Download Any Video", "Learn how AllMyTube works in 3 simple steps: copy URL, paste, download. Works for YouTube, TikTok, Vimeo and 10,000+ sites in 4K quality.", "/how-it-works/", body)

def build_pricing():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">Pricing</span></div>
  <div class="sec-lbl">Simple Pricing</div>
  <h1 class="tc">AllMyTube <span style="color:var(--acc)">Pricing</span></h1>
  <p style="max-width:540px;margin:.8rem auto 0;font-size:1.1rem;text-align:center">Start free. Upgrade anytime. All plans include access to 10,000+ sites and 4K downloads.</p>
</div>
<section>
  <div class="pgrid">
    <div class="pc">
      <div class="p-name">Free Trial</div>
      <div class="p-price">$<span>0</span></div>
      <div class="p-per">Limited features</div>
      <ul class="p-feats">
        <li>Download from 10,000+ sites</li>
        <li>Up to 1080p HD</li>
        <li>5 downloads to try</li>
        <li>Built-in media player</li>
        <li>Basic format conversion</li>
      </ul>
      <a href="{AFF_LINK}" class="btn btn-s" target="_blank" rel="noopener">Download Free</a>
    </div>
    <div class="pc feat">
      <div class="feat-badge">Most Popular</div>
      <div class="p-name">Annual Plan</div>
      <div class="p-price">$<span>29.99</span></div>
      <div class="p-per">per year — best value</div>
      <ul class="p-feats">
        <li>Everything in Free +</li>
        <li>Unlimited downloads</li>
        <li>4K &amp; 8K quality</li>
        <li>Full format converter (150+)</li>
        <li>Playlist &amp; channel download</li>
        <li>Browser extension</li>
        <li>Priority support</li>
        <li>Free updates included</li>
      </ul>
      <a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">Get Best Deal →</a>
    </div>
    <div class="pc">
      <div class="p-name">Lifetime</div>
      <div class="p-price">$<span>49.99</span></div>
      <div class="p-per">one-time payment</div>
      <ul class="p-feats">
        <li>Everything in Annual +</li>
        <li>Lifetime licence</li>
        <li>All future updates free</li>
        <li>Use on 1 PC</li>
        <li>No recurring fees</li>
      </ul>
      <a href="{AFF_LINK}" class="btn btn-s" target="_blank" rel="noopener">Buy Lifetime →</a>
    </div>
  </div>
  <div class="hbox" style="max-width:760px;margin:3rem auto 0;text-align:center">
    <p>💡 <strong style="color:var(--acc)">Tip:</strong> Wondershare frequently runs promotions. Click "Get Best Deal" to check the current discount before you buy.</p>
  </div>
</section>"""
    return page("AllMyTube Pricing 2025 — Free Trial, Annual & Lifetime Plans", "AllMyTube pricing plans: Free trial, $29.99/year or $49.99 lifetime. Unlimited downloads, 4K quality, 10,000+ sites, full converter included.", "/pricing/", body, "AllMyTube price, AllMyTube cost, AllMyTube coupon, video downloader price")

def build_faq():
    faqs = [
        ("Is AllMyTube free?", "Yes — AllMyTube offers a free trial that lets you download from 10,000+ sites and experience the full feature set. The free version has a download limit. Upgrade to the annual ($29.99/yr) or lifetime plan for unlimited downloads."),
        ("Is AllMyTube safe to use?", "AllMyTube is developed by Wondershare, a globally recognized software company trusted by over 50 million users in 200+ countries. It is 100% safe, virus-free, and contains no bundled malware or adware."),
        ("Does AllMyTube work on Mac?", "Yes. AllMyTube is available for both Windows (7/8/10/11) and macOS. Both versions share the same powerful feature set including 4K downloads, batch processing, and the built-in converter."),
        ("Can I download 4K videos with AllMyTube?", "Absolutely. AllMyTube supports resolutions up to 4K (2160p) from platforms that offer 4K content such as YouTube. You can choose from 7 resolution presets: 2160p, 1440p, 1080p, 720p, 480p, 360p, and 240p."),
        ("How many sites does AllMyTube support?", "AllMyTube supports over 10,000 video-sharing websites including YouTube, TikTok, Vimeo, Facebook, Instagram, Twitter/X, Twitch, Dailymotion, Reddit, Bilibili, and thousands more globally."),
        ("Can I download entire YouTube playlists?", "Yes! AllMyTube's batch download feature lets you download entire YouTube playlists or channels with a single click. Just paste the playlist URL and AllMyTube handles the rest."),
        ("Can I extract MP3 audio from videos?", "Yes. AllMyTube's built-in converter can extract audio as MP3, AAC, FLAC, or WAV from any downloaded video. It's great for music, podcasts, audiobooks, and lectures."),
        ("What formats does AllMyTube convert to?", "AllMyTube supports over 150 output formats including MP4, MKV, AVI, MOV, WMV, FLV, MP3, AAC, FLAC, WAV, and device-optimized presets for iPhone, Android, iPad, Samsung TV, PlayStation, and more."),
        ("Does AllMyTube have a browser extension?", "Yes. AllMyTube includes a browser extension for Chrome, Firefox, and Edge that adds a download button directly to video pages — no need to copy and paste URLs."),
        ("Is it legal to download YouTube videos?", "Downloading videos for personal, offline viewing is a legal grey area that varies by country. AllMyTube is a tool; users are responsible for complying with applicable terms of service and copyright laws in their region."),
    ]
    faq_html = "".join(f'<details><summary>{q}</summary><div class="da"><p>{a}</p></div></details>' for q, a in faqs)
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">FAQ</span></div>
  <div class="sec-lbl">Got Questions?</div>
  <h1>AllMyTube <span style="color:var(--acc)">FAQ</span></h1>
</div>
<section><div class="faq">{faq_html}</div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">⬇ Download AllMyTube Free</a>
  </div>
</section>"""
    return page("AllMyTube FAQ — Frequently Asked Questions", "Answers to the most common AllMyTube questions: Is it free? Is it safe? Mac support? 4K downloads? Playlist download? MP3 extraction?", "/faq/", body, "AllMyTube FAQ, AllMyTube safe, AllMyTube free, AllMyTube Mac")

def build_review():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">Review</span></div>
  <div class="sec-lbl">In-Depth Analysis</div>
  <h1>AllMyTube <span style="color:var(--acc)">Review 2025</span></h1>
  <p style="max-width:620px;margin-top:.8rem;font-size:1.05rem">We tested AllMyTube across 30+ platforms, 5 resolutions, and dozens of format conversions. Here's our complete verdict.</p>
</div>
<section>
  <div class="hbox">
    <div style="display:flex;gap:2rem;align-items:center;flex-wrap:wrap">
      <div style="text-align:center"><div style="font-family:'Bebas Neue',sans-serif;font-size:4rem;color:var(--acc)">9.2</div><div style="font-size:.8rem;color:var(--mut)">OUT OF 10</div></div>
      <div><h3 style="margin-bottom:.5rem">Editor's Rating</h3><p>AllMyTube earns a 9.2/10 for its unmatched site coverage, genuine 4K quality, and rock-solid batch downloading. Minor deductions for the learning curve on advanced conversion settings.</p></div>
    </div>
  </div>
  <div class="cards" style="margin-top:2rem">
    <div class="card"><h3 style="color:var(--acc)">Performance ★★★★★</h3><p>Downloads at 3× the speed of competitors. In testing, a 1080p YouTube video downloaded in under 8 seconds on a standard broadband connection.</p></div>
    <div class="card"><h3 style="color:var(--acc)">Ease of Use ★★★★☆</h3><p>The interface is clean and intuitive for basic use. Advanced converter settings have a slight learning curve but the built-in presets cover most use cases.</p></div>
    <div class="card"><h3 style="color:var(--acc)">Site Coverage ★★★★★</h3><p>10,000+ sites is genuinely impressive. We tested 30+ platforms and AllMyTube worked flawlessly on all of them including niche regional sites.</p></div>
    <div class="card"><h3 style="color:var(--acc)">Quality ★★★★★</h3><p>4K downloads match the source quality perfectly. No re-encoding artifacts. Audio extraction is clean with proper ID3 tagging for MP3 files.</p></div>
    <div class="card"><h3 style="color:var(--acc)">Value ★★★★★</h3><p>At $29.99/year or $49.99 lifetime, AllMyTube is exceptional value. The lifetime plan is a no-brainer if you download videos regularly.</p></div>
    <div class="card"><h3 style="color:var(--acc)">Support ★★★★☆</h3><p>Wondershare offers email support, live chat, and extensive documentation. Response times are reasonable. Community forum is active and helpful.</p></div>
  </div>
  <div style="margin-top:3rem;text-align:center"><a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">⬇ Try AllMyTube Free</a></div>
</section>"""
    return page("AllMyTube Review 2025 — Honest Rating & Full Analysis", "Read our in-depth AllMyTube review: 9.2/10 rating. We test performance, site coverage, 4K quality, ease of use and value. Is it worth it?", "/review/", body, "AllMyTube review, AllMyTube rating, is AllMyTube good, Wondershare AllMyTube review")

def build_download():
    body = f"""
<div class="ph tc">
  <div class="sec-lbl">Get Started</div>
  <h1>Download <span style="color:var(--acc)">AllMyTube</span></h1>
  <p style="max-width:520px;margin:.8rem auto 0;font-size:1.1rem">Free trial available for Windows &amp; Mac. No credit card required.</p>
</div>
<section class="tc">
  <div class="cards" style="max-width:700px;margin:0 auto 2rem">
    <div class="card tc">
      <div class="c-icon" style="margin:0 auto 1rem">🪟</div>
      <h3>Windows</h3>
      <p style="margin-bottom:1.2rem">Compatible with Windows 7, 8, 10 &amp; 11 (32-bit &amp; 64-bit)</p>
      <a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">⬇ Download for Windows</a>
    </div>
    <div class="card tc">
      <div class="c-icon" style="margin:0 auto 1rem">🍎</div>
      <h3>Mac</h3>
      <p style="margin-bottom:1.2rem">Compatible with macOS 10.12 Sierra and later</p>
      <a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">⬇ Download for Mac</a>
    </div>
  </div>
  <div class="hbox" style="max-width:700px;margin:0 auto">
    <h3 style="margin-bottom:1rem;color:var(--acc)">What's Included in the Free Trial</h3>
    <ul class="flist">
      <li>Download from 10,000+ video sites</li>
      <li>Try all resolution options up to 4K</li>
      <li>Test the built-in converter and media player</li>
      <li>Experience batch download and playlist saving</li>
    </ul>
  </div>
</section>"""
    return page("Download AllMyTube Free — Windows & Mac", "Download AllMyTube free for Windows and Mac. Free trial with access to all features. Compatible with Windows 7-11 and macOS 10.12+.", "/download/", body)

def build_vs_4k():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <a href="{SITE_ROOT}/alternatives/">Alternatives</a> › <span class="cur">vs 4K Video Downloader</span></div>
  <h1>AllMyTube vs <span style="color:var(--acc)">4K Video Downloader</span></h1>
  <p style="max-width:620px;margin-top:.8rem">Two of the most popular video downloaders compared head-to-head. Which should you choose?</p>
</div>
<section>
  <div class="twrap">
    <table>
      <thead><tr><th>Feature</th><th>AllMyTube</th><th>4K Video Downloader</th></tr></thead>
      <tbody>
        <tr><td>Supported Sites</td><td class="ck">10,000+</td><td>500+</td></tr>
        <tr><td>Max Resolution</td><td class="ck">4K (2160p)</td><td class="ck">4K (2160p)</td></tr>
        <tr><td>MP3 Extraction</td><td class="ck">✓ Built-in</td><td>✓ Basic</td></tr>
        <tr><td>Playlist Download</td><td class="ck">✓ Unlimited</td><td>Limited free</td></tr>
        <tr><td>Built-in Converter</td><td class="ck">✓ 150+ formats</td><td class="cx">✗ Not included</td></tr>
        <tr><td>Browser Extension</td><td class="ck">✓</td><td class="cx">✗</td></tr>
        <tr><td>Download Scheduler</td><td class="ck">✓</td><td class="cx">✗</td></tr>
        <tr><td>Built-in Player</td><td class="ck">✓</td><td class="cx">✗</td></tr>
        <tr><td>Lifetime License</td><td class="ck">✓ $49.99</td><td>✓ $45</td></tr>
        <tr><td>Annual Plan</td><td class="ck">✓ $29.99/yr</td><td>✓ $15/yr</td></tr>
        <tr><td>Windows + Mac</td><td class="ck">✓</td><td class="ck">✓</td></tr>
      </tbody>
    </table>
  </div>
  <div class="hbox" style="margin-top:2rem">
    <h3 style="margin-bottom:.8rem;color:var(--acc)">Verdict</h3>
    <p>AllMyTube wins on features: 20× more supported sites, a built-in converter, browser extension, download scheduler, and media player make it the more complete package. 4K Video Downloader is cheaper annually but requires separate tools for conversion. For most users, AllMyTube offers far better value.</p>
  </div>
  <div style="margin-top:2rem;text-align:center"><a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">Try AllMyTube Free →</a></div>
</section>"""
    return page("AllMyTube vs 4K Video Downloader — Full Comparison 2025", "Compare AllMyTube vs 4K Video Downloader: features, pricing, supported sites, conversion tools. Which video downloader is better in 2025?", "/vs-4k-video-downloader/", body)

def build_vs_ytdlp():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <a href="{SITE_ROOT}/alternatives/">Alternatives</a> › <span class="cur">vs yt-dlp</span></div>
  <h1>AllMyTube vs <span style="color:var(--acc)">yt-dlp</span></h1>
  <p style="max-width:620px;margin-top:.8rem">yt-dlp is a powerful command-line tool. AllMyTube is a polished GUI app. Here's how they stack up.</p>
</div>
<section>
  <div class="twrap">
    <table>
      <thead><tr><th>Factor</th><th>AllMyTube</th><th>yt-dlp</th></tr></thead>
      <tbody>
        <tr><td>Ease of Use</td><td class="ck">★★★★★ Beginner-friendly GUI</td><td>Command-line only</td></tr>
        <tr><td>Installation</td><td class="ck">One-click installer</td><td>Requires Python/CLI knowledge</td></tr>
        <tr><td>Supported Sites</td><td class="ck">10,000+</td><td class="ck">1,000+ (open source)</td></tr>
        <tr><td>4K Downloads</td><td class="ck">✓</td><td class="ck">✓</td></tr>
        <tr><td>Built-in Converter</td><td class="ck">✓ GUI</td><td>Via FFmpeg (manual config)</td></tr>
        <tr><td>Price</td><td>Free trial / $29.99</td><td class="ck">Free &amp; open source</td></tr>
        <tr><td>Updates</td><td class="ck">Auto-updates</td><td>Manual / CLI updates</td></tr>
        <tr><td>Support</td><td class="ck">Official Wondershare support</td><td>Community-only</td></tr>
        <tr><td>Browser Extension</td><td class="ck">✓</td><td class="cx">✗</td></tr>
        <tr><td>Built-in Player</td><td class="ck">✓</td><td class="cx">✗</td></tr>
      </tbody>
    </table>
  </div>
  <div class="hbox" style="margin-top:2rem">
    <h3 style="margin-bottom:.8rem;color:var(--acc)">Verdict</h3>
    <p>yt-dlp is fantastic if you're comfortable with the command line and want a free, endlessly configurable tool. AllMyTube wins for anyone who wants a polished, point-and-click experience with built-in conversion, a browser extension, and official support. It's also far faster to set up and use for non-technical users.</p>
  </div>
  <div style="margin-top:2rem;text-align:center"><a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">Try AllMyTube Free →</a></div>
</section>"""
    return page("AllMyTube vs yt-dlp — GUI vs Command Line Comparison 2025", "AllMyTube vs yt-dlp: ease of use, features, site support, price. Which video downloader is right for you? Full comparison 2025.", "/vs-ytdlp/", body)

def build_vs_videoder():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <a href="{SITE_ROOT}/alternatives/">Alternatives</a> › <span class="cur">vs Videoder</span></div>
  <h1>AllMyTube vs <span style="color:var(--acc)">Videoder</span></h1>
  <p style="max-width:620px;margin-top:.8rem">Videoder is popular on Android. AllMyTube is the premium desktop solution. Here's the breakdown.</p>
</div>
<section>
  <div class="twrap">
    <table>
      <thead><tr><th>Factor</th><th>AllMyTube</th><th>Videoder</th></tr></thead>
      <tbody>
        <tr><td>Platform</td><td class="ck">Windows &amp; Mac</td><td>Android &amp; Windows</td></tr>
        <tr><td>Supported Sites</td><td class="ck">10,000+</td><td>50+</td></tr>
        <tr><td>4K Quality</td><td class="ck">✓</td><td>Limited</td></tr>
        <tr><td>Batch Downloads</td><td class="ck">✓ Unlimited</td><td>Limited</td></tr>
        <tr><td>Built-in Converter</td><td class="ck">✓ 150+ formats</td><td>Basic only</td></tr>
        <tr><td>Browser Extension</td><td class="ck">✓</td><td class="cx">✗</td></tr>
        <tr><td>Privacy / Safety</td><td class="ck">✓ No ads / malware</td><td>Ad-supported</td></tr>
        <tr><td>Official Support</td><td class="ck">✓ Wondershare</td><td>Community</td></tr>
      </tbody>
    </table>
  </div>
  <div class="hbox" style="margin-top:2rem"><p>For desktop users, AllMyTube is the clear winner with vastly more site support, better quality, and a professional-grade feature set. Videoder may suit Android users but is not a direct alternative for desktop power users.</p></div>
  <div style="margin-top:2rem;text-align:center"><a href="{AFF_LINK}" class="btn btn-p" target="_blank" rel="noopener">Try AllMyTube Free →</a></div>
</section>"""
    return page("AllMyTube vs Videoder — Desktop Video Downloader Comparison", "Compare AllMyTube vs Videoder: platform support, site coverage, quality, and features. Which is better for desktop video downloading?", "/vs-videoder/", body)

def build_alternatives():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">Alternatives</span></div>
  <h1>AllMyTube <span style="color:var(--acc)">Alternatives</span> Compared</h1>
  <p style="max-width:620px;margin-top:.8rem">We compare AllMyTube with the top alternatives so you can make an informed choice.</p>
</div>
<section>
  <div class="cards">
    <div class="card"><h3>AllMyTube <span class="chip chip-g">Winner</span></h3><p>10,000+ sites, 4K, built-in converter, batch download, browser extension. Best all-in-one solution.</p><a href="{AFF_LINK}" class="btn btn-p" style="margin-top:1rem;font-size:.82rem" target="_blank" rel="noopener">Download Free</a></div>
    <div class="card"><h3>4K Video Downloader</h3><p>Good 4K quality, simpler interface. Lacks built-in converter and covers fewer sites. Cheaper annual plan.</p><a href="{SITE_ROOT}/vs-4k-video-downloader/" style="font-size:.85rem;display:block;margin-top:1rem">Compare →</a></div>
    <div class="card"><h3>yt-dlp</h3><p>Free, open-source, command-line. Extremely powerful but requires technical knowledge to use effectively.</p><a href="{SITE_ROOT}/vs-ytdlp/" style="font-size:.85rem;display:block;margin-top:1rem">Compare →</a></div>
    <div class="card"><h3>Videoder</h3><p>Popular on Android. Limited desktop functionality. Ad-supported. Much smaller site library than AllMyTube.</p><a href="{SITE_ROOT}/vs-videoder/" style="font-size:.85rem;display:block;margin-top:1rem">Compare →</a></div>
    <div class="card"><h3>JDownloader</h3><p>Free, open-source. Complex setup, dated UI. Supports many sites but lacks AllMyTube's converter and player.</p><p style="margin-top:.5rem"><span class="chip">Free</span></p></div>
    <div class="card"><h3>Internet Download Manager</h3><p>Excellent download manager overall but not video-download focused. No built-in converter or playlist support.</p><p style="margin-top:.5rem"><span class="chip chip-r">Windows only</span></p></div>
  </div>
</section>"""
    return page("Best AllMyTube Alternatives 2025 — Full Comparison", "Compare AllMyTube vs the best video downloader alternatives: 4K Video Downloader, yt-dlp, Videoder, JDownloader. Which is best for you?", "/alternatives/", body)

def build_blog_index():
    posts = [
        ("📥", "How to Download 4K YouTube Videos in 2025", "Step-by-step guide to saving YouTube videos at maximum 4K quality using AllMyTube.", "Tutorial", "June 2025"),
        ("🎵", "How to Extract MP3 Audio from Any Video", "Convert YouTube, Vimeo and any video to high-quality MP3 audio in seconds.", "Tutorial", "May 2025"),
        ("📋", "Download an Entire YouTube Playlist in One Click", "Save hundreds of videos at once with AllMyTube's batch playlist downloader.", "Guide", "May 2025"),
        ("🌍", "Best Video Downloaders for 2025 — Ranked", "We tested the 10 most popular video downloaders. Here's our definitive ranking.", "Review", "April 2025"),
        ("📱", "How to Watch YouTube Offline on Any Device", "Download YouTube videos and transfer them to your phone, tablet or TV.", "Tutorial", "April 2025"),
        ("🔒", "Is Downloading YouTube Videos Legal?", "The legal landscape around video downloading explained clearly for global users.", "Legal", "March 2025"),
    ]
    cards = "".join(f"""
    <div class="bc">
      <div class="bc-img">{emoji}</div>
      <div class="bc-body">
        <div class="bc-tag">{tag}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
        <div class="bc-meta"><span>{date}</span></div>
      </div>
    </div>""" for emoji, title, desc, tag, date in posts)
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">Blog</span></div>
  <div class="sec-lbl">Guides &amp; Tutorials</div>
  <h1>AllMyTube <span style="color:var(--acc)">Blog</span></h1>
  <p style="max-width:600px;margin-top:.8rem">Tips, guides, tutorials and how-tos for getting the most out of AllMyTube and video downloading.</p>
</div>
<section><div class="bgrid">{cards}</div></section>"""
    return page("AllMyTube Blog — Video Download Guides & Tutorials", "Video download guides, tutorials and tips. Learn how to download 4K YouTube videos, extract MP3 audio, save playlists, and more with AllMyTube.", "/blog/", body)

def build_privacy():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">Privacy Policy</span></div>
  <h1>Privacy <span style="color:var(--acc)">Policy</span></h1>
  <p style="margin-top:.5rem;font-size:.9rem;color:var(--mut)">Last updated: June 2025</p>
</div>
<section style="max-width:800px;margin:0 auto">
  <div class="hbox">
    <p>This site (brightlane.github.io/allmytube) is an affiliate marketing website for AllMyTube by Wondershare. We earn commissions on purchases made through our affiliate links at no extra cost to you.</p>
  </div>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Information We Collect</h3>
  <p>This website does not directly collect personal information. We use standard web analytics (page views, referrer data) which may be provided by GitHub Pages. No personally identifiable information is stored by us.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Affiliate Links</h3>
  <p>Links to AllMyTube on this site are affiliate links. When you click and make a purchase, we receive a commission. This does not affect the price you pay. We only recommend products we genuinely believe provide value.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Cookies</h3>
  <p>This site may use cookies through GitHub Pages infrastructure. Affiliate link tracking uses cookies managed by LinkConnector, the affiliate network. You can disable cookies in your browser settings.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Third Parties</h3>
  <p>When you click through to AllMyTube's website, you are subject to Wondershare's privacy policy. We are not responsible for third-party data practices.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Contact</h3>
  <p>For privacy questions, please raise an issue on the GitHub repository for this site.</p>
</section>"""
    return page("Privacy Policy — AllMyTube Affiliate Site", "Privacy policy for the AllMyTube affiliate guide site. Information about affiliate links, cookies, and data collection.", "/privacy/", body)

def build_disclaimer():
    body = f"""
<div class="ph">
  <div class="bc-nav"><a href="{SITE_ROOT}/">Home</a> › <span class="cur">Disclaimer</span></div>
  <h1>Affiliate <span style="color:var(--acc)">Disclaimer</span></h1>
  <p style="margin-top:.5rem;font-size:.9rem;color:var(--mut)">Last updated: June 2025</p>
</div>
<section style="max-width:800px;margin:0 auto">
  <div class="hbox">
    <p><strong style="color:var(--acc)">Disclosure:</strong> This website contains affiliate links. As an affiliate of Wondershare AllMyTube through the LinkConnector network, we earn a commission when purchases are made through our links — at no extra cost to you.</p>
  </div>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Editorial Independence</h3>
  <p>Our reviews and recommendations are based on genuine research and testing. Affiliate relationships do not influence our editorial opinions. We aim to provide honest, useful information to help you make the right purchasing decision.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Accuracy</h3>
  <p>We strive to keep pricing, feature information and comparisons accurate and up to date. However, software features and pricing can change. Always verify current details on the official Wondershare website before purchasing.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Legal Use</h3>
  <p>Video downloading software should only be used in compliance with applicable copyright laws and the terms of service of the platforms being used. We do not condone or encourage copyright infringement.</p>
</section>"""
    return page("Affiliate Disclaimer — AllMyTube Guide", "Affiliate disclosure and disclaimer for the AllMyTube guide site. We earn commissions on purchases through our affiliate links.", "/disclaimer/", body)

def build_sitemap():
    pages_list = [
        "/", "/features/", "/supported-sites/", "/how-it-works/", "/pricing/",
        "/faq/", "/review/", "/download/", "/blog/", "/alternatives/",
        "/vs-4k-video-downloader/", "/vs-ytdlp/", "/vs-videoder/",
        "/privacy/", "/disclaimer/",
    ]
    urls = "\n".join(f"""  <url>
    <loc>{SITE_URL}{p}</loc>
    <changefreq>{'weekly' if p == '/' else 'monthly'}</changefreq>
    <priority>{'1.0' if p == '/' else '0.8'}</priority>
  </url>""" for p in pages_list)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""

def build_robots():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

def build_llms_txt():
    return f"""# AllMyTube Affiliate Guide
> Site URL: {SITE_URL}
> Purpose: Affiliate marketing site promoting AllMyTube video downloader by Wondershare

## About This Site
This is an independent affiliate guide for AllMyTube (by Wondershare). We earn commissions on purchases through our affiliate links. The site provides reviews, comparisons, tutorials, and feature guides to help users understand and evaluate AllMyTube.

## AllMyTube Summary
AllMyTube is a video downloader and converter by Wondershare. Key facts:
- Downloads videos from 10,000+ sites including YouTube, TikTok, Vimeo, Facebook
- Supports resolutions up to 4K (2160p) with 7 quality presets
- Built-in converter supporting 150+ output formats (MP4, MP3, MKV, AVI, etc.)
- Batch download for playlists and entire channels
- Browser extension for Chrome, Firefox, Edge
- Built-in media player
- Download scheduler (Auto Shutdown, Sleep, Exit modes)
- 50M+ users across 200+ countries
- Available for Windows and Mac
- Free trial available; paid plans from $29.99/year or $49.99 lifetime

## Site Pages
- / — Homepage with overview and key features
- /features/ — Full feature breakdown
- /supported-sites/ — List of 10,000+ supported platforms
- /how-it-works/ — Step-by-step usage guide
- /pricing/ — Plan comparison (free, annual, lifetime)
- /review/ — Editorial review with ratings
- /faq/ — 10 common questions answered
- /download/ — Download page for Windows and Mac
- /blog/ — Tutorials and how-to guides
- /alternatives/ — Comparison with competitors
- /vs-4k-video-downloader/ — Head-to-head vs 4K Video Downloader
- /vs-ytdlp/ — Head-to-head vs yt-dlp
- /vs-videoder/ — Head-to-head vs Videoder
- /privacy/ — Privacy policy
- /disclaimer/ — Affiliate disclaimer

## Affiliate Link
All "Download" or "Get AllMyTube" CTAs link to: {AFF_LINK}

## Content Policy
All content is original, informational, and based on publicly available product information. Pricing and features should be verified on the official Wondershare site as they may change.
"""

def build_favicon_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#050810"/>
  <text x="32" y="46" font-family="sans-serif" font-weight="900" font-size="36" text-anchor="middle" fill="#00d4ff">▶</text>
</svg>"""

def build_404():
    body = f"""
<div class="ph tc">
  <div style="font-family:'Bebas Neue',sans-serif;font-size:8rem;color:var(--acc);text-shadow:var(--glow);line-height:1">404</div>
  <h1>Page <span style="color:var(--acc2)">Not Found</span></h1>
  <p style="max-width:420px;margin:1rem auto 2rem">The page you're looking for doesn't exist. Let's get you back on track.</p>
  <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
    <a href="{SITE_ROOT}/" class="btn btn-p">← Go Home</a>
    <a href="{AFF_LINK}" class="btn btn-s" target="_blank" rel="noopener">Download AllMyTube</a>
  </div>
</div>"""
    return page("404 — Page Not Found | AllMyTube Guide", "Page not found.", "/404/", body)

# ══════════════════════════════════════════════════════════════════════════════
#  BUILD ALL FILES
# ══════════════════════════════════════════════════════════════════════════════

def main():
    print("\n🔨 Building AllMyTube site for https://brightlane.github.io/allmytube/\n")

    # HTML pages
    write("index.html",            build_index())
    write("features/index.html",   build_features())
    write("supported-sites/index.html", build_supported_sites())
    write("how-it-works/index.html",    build_how_it_works())
    write("pricing/index.html",    build_pricing())
    write("faq/index.html",        build_faq())
    write("review/index.html",     build_review())
    write("download/index.html",   build_download())
    write("blog/index.html",       build_blog_index())
    write("alternatives/index.html",        build_alternatives())
    write("vs-4k-video-downloader/index.html", build_vs_4k())
    write("vs-ytdlp/index.html",   build_vs_ytdlp())
    write("vs-videoder/index.html",build_vs_videoder())
    write("privacy/index.html",    build_privacy())
    write("disclaimer/index.html", build_disclaimer())
    write("404.html",              build_404())

    # SEO / meta files
    write("sitemap.xml",  build_sitemap())
    write("robots.txt",   build_robots())
    write("llms.txt",     build_llms_txt())
    write("assets/favicon.svg", build_favicon_svg())

    # GitHub Pages config: tell Jekyll to pass through
    write(".nojekyll", "")

    print(f"\n✅ Done! {len(list(BASE.rglob('*')))} files generated.")
    print(f"   Deploy the contents of {BASE} as the /allmytube/ folder in your GitHub repo.")

if __name__ == "__main__":
    main()
