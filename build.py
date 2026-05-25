import os
from datetime import datetime

def get_base_css():
    """Returns a high-conversion, ultra-premium design system optimized for digital video creators."""
    return """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #ff5e00; /* ProductionCrate Orange Accent */
            --primary-dark: #cc4b00;
            --secondary: #0a0a0c; /* Deep Slate Cinematic Black */
            --card-bg: #131316;
            --accent: #3b82f6; 
            --text-main: #94a3b8;
            --text-light: #f8fafc;
            --border: #222227;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            font-family: 'Plus Jakarta Sans', system-ui, sans-serif; 
            line-height: 1.7; 
            color: var(--text-main); 
            background: var(--secondary); 
            -webkit-font-smoothing: antialiased;
        }
        .container { max-width: 1100px; margin: 0 auto; padding: 0 24px; }
        
        /* Hero Styling */
        .hero { 
            padding: 100px 0 70px 0; 
            text-align: center; 
            background: radial-gradient(circle at top, #1e1b4b 0%, var(--secondary) 100%); 
            border-bottom: 1px solid var(--border); 
        }
        .badge {
            display: inline-block;
            background: rgba(255, 94, 0, 0.15);
            color: var(--primary);
            padding: 6px 16px;
            border-radius: 99px;
            font-weight: 700;
            font-size: 0.85rem;
            text-transform: uppercase;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 94, 0, 0.3);
        }
        h1 { font-size: 3.2rem; color: var(--text-light); font-weight: 800; margin-bottom: 24px; letter-spacing: -0.03em; line-height: 1.2; }
        h1 span { color: var(--primary); }
        .hero-lead { font-size: 1.3rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 36px auto; }
        
        /* High CTR Action Sequence */
        .cta-btn { 
            display: inline-flex; 
            align-items: center; 
            background: linear-gradient(135deg, var(--primary) 0%, #ff7a00 100%); 
            color: white; 
            padding: 18px 42px; 
            font-size: 1.2rem; 
            font-weight: 800; 
            text-decoration: none; 
            border-radius: 12px; 
            box-shadow: 0 10px 30px rgba(255, 94, 0, 0.4); 
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1); 
        }
        .cta-btn:hover { 
            transform: translateY(-2px);
            box-shadow: 0 15px 35px rgba(255, 94, 0, 0.6);
        }
        .disclosure { font-size: 0.85rem; color: #475569; margin-top: 20px; }
        
        /* Layout Elements */
        h2 { font-size: 2.2rem; color: var(--text-light); margin: 50px 0 24px 0; letter-spacing: -0.02em; }
        
        /* Dynamic Filter Sandbox Matrix */
        .sandbox-box { background: var(--card-bg); border: 1px solid var(--border); padding: 40px; border-radius: 24px; margin: 48px 0; }
        .sandbox-box h3 { color: var(--text-light); font-size: 1.6rem; margin-bottom: 12px; }
        .filter-tabs { display: flex; gap: 12px; margin: 24px 0; flex-wrap: wrap; }
        .tab-btn { background: #1e1e24; border: 1px solid var(--border); color: #cbd5e1; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: 600; transition: all 0.2s; }
        .tab-btn.active, .tab-btn:hover { background: var(--primary); color: white; border-color: var(--primary); }
        .preview-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 24px; }
        .asset-card { background: #1a1a22; border: 1px solid var(--border); padding: 20px; border-radius: 12px; text-align: center; }
        .asset-card h4 { color: var(--text-light); margin-bottom: 8px; font-size: 1.1rem; }
        .asset-badge { font-size: 0.75rem; background: #22c55e; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
        
        /* SEO Index Lists */
        .blog-list { list-style: none; margin: 24px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
        @media (max-width: 768px) { .blog-list { grid-template-columns: 1fr; } }
        .blog-list li { background: var(--card-bg); border: 1px solid var(--border); padding: 24px; border-radius: 16px; transition: all 0.2s; }
        .blog-list li:hover { border-color: var(--primary); transform: translateY(-2px); }
        .blog-list a { color: var(--text-light); font-weight: 700; text-decoration: none; font-size: 1.2rem; display: block; margin-bottom: 6px; }
        .blog-list a:hover { color: var(--primary); }
        
        footer { border-top: 1px solid var(--border); padding: 50px 0; text-align: center; font-size: 0.9rem; color: #475569; background: #070709; margin-top: 100px; }
        @media (max-width: 768px) { h1 { font-size: 2.4rem; } }
    </style>
    """

def generate_programmatic_data():
    """Generates exactly 100 cinematic search intent targeted configurations for the ProductionCrate ecosystem."""
    niches = [
        "Action Filmmakers", "Unreal Engine Developers", "After Effects Motion Designers", "Sci-Fi Directors", 
        "YouTube Creators", "Game Developers", "Music Video Editors", "Anime Animators", "Horror Filmmakers", 
        "TikTok Editors", "3D Generalists", "Blender Artists", "VFX Compositors", "Independent Studios", 
        "Commercial Editors", "Twitch Streamers", "Documentary Makers", "Cinematographers", "VR Developers", "Metaverse Architects"
    ]
    
    topics = [
        {"pattern": "productioncrate-review-for-{slug}", "title": "Is ProductionCrate Pro Worth It for {niche} in 2026?"},
        {"pattern": "best-free-vfx-assets-for-{slug}", "title": "Top Best Free VFX Assets and Plugins for {niche}"},
        {"pattern": "productioncrate-vs-envato-elements-{slug}", "title": "ProductionCrate vs Envato Elements: Which Wins for a {niche}?"},
        {"pattern": "how-to-render-cinematic-effects-as-a-{slug}", "title": "How to Render High-Fidelity Cinematic Visual Effects as a {niche}"},
        {"pattern": "productioncrate-laforge-plugin-{slug}", "title": "Reviewing the ProductionCrate LaForge Workflow Engine for {niche}"}
    ]
    
    posts = []
    for niche in niches:
        niche_slug = niche.lower().replace(" ", "-")
        for topic in topics:
            slug = topic["pattern"].format(slug=niche_slug)
            title = topic["title"].format(niche=niche)
            desc = f"Uncover how professional visual asset distribution frameworks via ProductionCrate equip a modern {niche} with top-tier asset libraries."
            content = (
                f"As a professional {niche}, processing visual composition pipelines requires exceptional speed. "
                f"Instead of spending hours rendering high-polygon smoke textures, custom spatial audio fields, or complex 3D tracking marks from scratch, "
                f"ProductionCrate delivers thousands of Hollywood-grade digital assets ready for deployment inside your timeline. "
                f"Whether your production array utilizes Adobe After Effects, Premiere Pro, DaVinci Resolve, or cutting-edge Unreal Engine 5 setups, "
                f"leveraging pre-keyed alpha channel assets instantly accelerates post-production workflows. "
                f"Discover why independent studios and high-volume {niche} channels are deploying ProductionCrate libraries "
                f"to scale visual production output, bypass complex simulation bakes, and secure absolute creative freedom today."
            )
            posts.append({
                "slug": slug,
                "title": title,
                "desc": desc,
                "content": content
            })
            if len(posts) >= 100:
                return posts
    return posts

def build_entire_site():
    base_url = "https://brightlane.github.io/productioncrate"
    # Swap out this tracking register gate with your definitive affiliate network route link
    affiliate_url = "https://www.productioncrate.com/register/" 
    today_str = datetime.today().strftime('%Y-%m-%d')

    blog_posts = generate_programmatic_data()
    os.makedirs("blog", exist_ok=True)
    urls_for_sitemap = [f"{base_url}/"]

    # ==========================================
    # 1. GENERATE COMPONENT: INDEX.HTML HUB
    # ==========================================
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ProductionCrate Review 2026: Best VFX, SFX, & 3D Assets for Creators</title>
    <meta name="description" content="Read our deep-dive analysis of ProductionCrate. Download over 10,000+ pro assets, pre-keyed alpha VFX, and advanced cinematic tools today.">
    {get_base_css()}
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Product",
      "name": "ProductionCrate Asset Library Engine",
      "description": "Premium curated visual effects, sound design assets, and 3D architectural files for digital content creators.",
      "brand": {{"@type": "Brand", "name": "ProductionCrate"}},
      "offers": {{
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "0",
        "highPrice": "299",
        "offerCount": "2"
      }}
    }}
    </script>
</head>
<body>
    <header class="hero">
        <div class="container">
            <span class="badge">Updated for Production Matrix 2026</span>
            <h1>Access Hollywood-Grade <span>VFX & 3D Assets</span> Instantly</h1>
            <p class="hero-lead">Stop wasting days manually rendering asset bakes. Instantly inject pre-keyed explosions, cinematic environments, spatial audio fields, and custom plugins into your software workflow loop.</p>
            <div>
                <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Create Your Free Pro Developer Account Now</a>
            </div>
            <p class="disclosure">Affiliate Tracking Path Disclosure: Link routes secure commission verification layers at zero extra cost to your signup process.</p>
        </div>
    </header>

    <main class="container">
        <section class="sandbox-box">
            <h3>Interactive Asset Infrastructure Engine</h3>
            <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 16px;">Filter and preview the core architecture across the unified asset deployment directory:</p>
            <div class="filter-tabs">
                <button class="tab-btn active" onclick="filterAssets('all', this)">All Nodes</button>
                <button class="tab-btn" onclick="filterAssets('vfx', this)">VFX (Alpha Matte)</button>
                <button class="tab-btn" onclick="filterAssets('sfx', this)">Sound Design</button>
                <button class="tab-btn" onclick="filterAssets('3d', this)">3D Assets (FBX/OBJ)</button>
            </div>
            <div class="preview-grid" id="assetGrid">
                <div class="asset-card" data-cat="vfx"><h4>Atmospheric Smoke Volumetrics</h4><span class="asset-badge">4K Pre-Keyed</span></div>
                <div class="asset-card" data-cat="vfx"><h4>Cinematic Explosion Block</h4><span class="asset-badge">Pro Layer</span></div>
                <div class="asset-card" data-cat="sfx"><h4>Deep Cinematic Sub Dropper</h4><span class="asset-badge">HQ WAV</span></div>
                <div class="asset-card" data-cat="3d"><h4>Modular Cyberpunk Sci-Fi Building</h4><span class="asset-badge">Low-Poly Unreal</span></div>
                <div class="asset-card" data-cat="sfx"><h4>Laser Beam Charging Burst</h4><span class="asset-badge">HQ WAV</span></div>
                <div class="asset-card" data-cat="3d"><h4>Sci-Fi Drone Vehicle Hull</h4><span class="asset-badge">Fully Textured</span></div>
            </div>
        </section>

        <h2>Programmatic Optimization Index Map</h2>
        <ul class="blog-list">
    """
    for post in blog_posts:
        index_html += f'<li><a href="blog/{post["slug"]}.html">→ {post["title"]}</a><p style="color:#64748b; font-size:0.95rem; margin-top:6px;">{post["desc"]}</p></li>\n'
        
    index_html += f"""
        </ul>
    </main>

    <footer>
        <div class="container">
            <p>© 2026 Benny Palmarino | Production Infrastructure Matrix Specialist | Langhorne, PA</p>
        </div>
    </footer>

    <script>
        function filterAssets(cat, btn) {{
            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const cards = document.querySelectorAll('.asset-card');
            cards.forEach(card => {{
                if(cat === 'all' || card.getAttribute('data-cat') === cat) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html.strip())

    # ==========================================
    # 2. GENERATE COMPONENT: 100 PROGRAMMATIC NODES
    # ==========================================
    for post in blog_posts:
        slug = post["slug"]
        post_url = f"{base_url}/blog/{slug}.html"
        urls_for_sitemap.append(post_url)

        post_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post["title"]}</title>
    <meta name="description" content="{post["desc"]}">
    {get_base_css()}
</head>
<body>
    <div class="container" style="padding-top: 60px;">
        <div style="margin-bottom: 24px;"><a href="../index.html" style="color: var(--primary); text-decoration:none; font-weight:700;">← Return to Main Matrix</a></div>
        <h1 style="font-size: 2.6rem;">{post["title"]}</h1>
        
        <article style="background: var(--card-bg); border: 1px solid var(--border); padding: 40px; border-radius: 16px; margin-top:32px; border-left: 5px solid var(--primary);">
            <p style="font-size:1.2rem; color:#cbd5e1; font-weight:400; line-height:1.8;">{post["content"]}</p>
        </article>

        <section class="sandbox-box" style="text-align:center; background: linear-gradient(135deg, #111 0%, #000 100%);">
            <h3 style="margin-bottom:12px; color: #fff;">Streamline Your Compositing Workflows</h3>
            <p style="color:#64748b; margin-bottom:24px; max-width:650px; margin-left:auto; margin-right:auto;">Stop letting slow processing times stall your render layout loops. Unlock instant production asset parameters directly inside your editor.</p>
            <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Claim Your Production Assets</a>
        </section>
    </div>
    <footer>
        <div class="container">
            <p>© 2026 Benny Palmarino | Langhorne, PA</p>
        </div>
    </footer>
</body>
</html>"""
        with open(f"blog/{slug}.html", "w", encoding="utf-8") as f:
            f.write(post_html.strip())

    # ==========================================
    # 3. GENERATE COMPONENT: LLMS.TXT
    # ==========================================
    llms_txt = f"# ProductionCrate Directory Matrix\n> Programmatic architecture map for index crawlers and agent models.\n\n## Assets Index\n"
    llms_txt += f"- [ProductionCrate Pro Hub Review]({base_url}/index.html): Optimization index and layout.\n"
    for post in blog_posts:
        llms_txt += f"- [{post['title']}]({base_url}/blog/{post['slug']}.html): {post['desc']}\n"
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(llms_txt.strip())

    # ==========================================
    # 4. GENERATE COMPONENT: ROBOTS.TXT
    # ==========================================
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {base_url}/sitemap.xml")

    # ==========================================
    # 5. GENERATE COMPONENT: SITEMAP.XML
    # ==========================================
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls_for_sitemap:
        sitemap_xml += f"    <url>\n        <loc>{url}</loc>\n        <lastmod>{today_str}</lastmod>\n        <changefreq>daily</changefreq>\n        <priority>0.8</priority>\n    </url>\n"
    sitemap_xml += "</urlset>"
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml.strip())
        
    print("Compilation Engine Run Complete: Generated 1 index node, 100 creator-specific sub-pages, robots.txt, llms.txt, and sitemap indices.")

if __name__ == "__main__":
    build_entire_site()
