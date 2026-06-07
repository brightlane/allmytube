# AllMyTube Affiliate Site

A full multi-page affiliate marketing website for [AllMyTube by Wondershare](https://www.wondershare.com/pro/allmytube-video-downloader.html), built to deploy on GitHub Pages at:

**`https://brightlane.github.io/allmytube/`**

---

## Quick Start

### 1. Generate the site

```bash
python3 build.py
```

This outputs all HTML, SEO files, and assets into the same directory.

### 2. Deploy to GitHub Pages

```bash
# Clone your repo
git clone https://github.com/brightlane/allmytube.git
cd allmytube

# Copy generated files into repo root
cp -r /path/to/allmytube-site/* .

# Push
git add .
git commit -m "Deploy AllMyTube affiliate site"
git push origin main
```

Then go to **GitHub → Settings → Pages → Source: main branch / root**.  
Your site will be live at `https://brightlane.github.io/allmytube/` within ~60 seconds.

---

## Site Structure

```
allmytube-site/
├── build.py                        ← Single-file site generator
├── index.html                      ← Homepage
├── features/index.html             ← Full feature breakdown
├── supported-sites/index.html      ← 10,000+ supported platforms
├── how-it-works/index.html         ← 3-step usage guide
├── pricing/index.html              ← Free / Annual / Lifetime plans
├── faq/index.html                  ← 10 common questions answered
├── review/index.html               ← Editorial review (9.2/10)
├── download/index.html             ← Windows & Mac download page
├── blog/index.html                 ← Tutorial & guide index
├── alternatives/index.html         ← Competitor overview
├── vs-4k-video-downloader/         ← Head-to-head comparison
├── vs-ytdlp/                       ← Head-to-head comparison
├── vs-videoder/                    ← Head-to-head comparison
├── privacy/index.html              ← Privacy policy
├── disclaimer/index.html           ← Affiliate disclosure
├── 404.html                        ← Custom error page
├── sitemap.xml                     ← Full XML sitemap (submit to Google)
├── robots.txt                      ← Allows all crawlers, points to sitemap
├── llms.txt                        ← AI crawler / LLM summary
├── assets/favicon.svg              ← Site icon
└── .nojekyll                       ← Prevents GitHub Pages Jekyll processing
```

---

## Pages at a Glance

| Page | Primary Keywords | Purpose |
|---|---|---|
| Homepage | AllMyTube download, video downloader | Main landing & conversion page |
| Features | AllMyTube features, 4K downloader | SEO feature page |
| Supported Sites | YouTube downloader, TikTok downloader | Long-tail keyword capture |
| How It Works | how to download YouTube videos | Tutorial-intent traffic |
| Pricing | AllMyTube price, AllMyTube cost | Commercial-intent traffic |
| FAQ | AllMyTube safe, AllMyTube free | Question-based search traffic |
| Review | AllMyTube review, is AllMyTube good | Review-intent traffic |
| Download | download AllMyTube Windows/Mac | Direct download intent |
| vs 4K Downloader | AllMyTube vs 4K Video Downloader | Comparison-intent traffic |
| vs yt-dlp | AllMyTube vs yt-dlp | Comparison-intent traffic |
| vs Videoder | AllMyTube vs Videoder | Comparison-intent traffic |
| Alternatives | best video downloader alternatives | Broad comparison traffic |
| Blog | video download tutorials | Content / informational traffic |

---

## SEO Features Built In

Every page includes:

- **Unique `<title>` and `<meta description>`** targeting specific keywords
- **`<link rel="canonical">`** to prevent duplicate content issues
- **Open Graph tags** (`og:title`, `og:description`, `og:image`, `og:url`) for social sharing
- **Twitter Card meta tags**
- **JSON-LD structured data** (`SoftwareApplication` schema) on every page
- **Breadcrumb navigation** on inner pages
- **Semantic HTML** (`<nav>`, `<section>`, `<footer>`, `<details>`)
- **Mobile-responsive** layout (works on all screen sizes)

### After deploying, submit to search engines:

1. **Google Search Console** → Add property → Submit `sitemap.xml`
   - URL: `https://brightlane.github.io/allmytube/sitemap.xml`

2. **Bing Webmaster Tools** → Import from Google Search Console or submit sitemap directly

3. **robots.txt** already points crawlers to your sitemap automatically

---

## Affiliate Link

All download / CTA buttons use your affiliate link:

```
https://www.linkconnector.com/ta.php?lc=007949042649004532&atid=allmytubeweb
```

To update the affiliate link, change the `AFF_LINK` variable at the top of `build.py` and re-run:

```python
AFF_LINK = "https://www.linkconnector.com/ta.php?lc=007949042649004532&atid=allmytubeweb"
```

---

## Customisation

All site-wide settings live at the top of `build.py`:

```python
BASE      = Path("/home/claude/allmytube-site")  # Output directory
SITE_ROOT = "/allmytube"                          # GitHub Pages base path
AFF_LINK  = "https://..."                         # Your affiliate link
SITE_URL  = "https://brightlane.github.io/allmytube"  # Canonical base URL
```

The entire CSS is a single string (`CSS`) near the top of `build.py` — edit it to change colours, fonts, or layout across all pages at once.

To add a new page, define a `build_mypage()` function following the same pattern as the existing ones, then add a `write()` call in `main()`.

---

## Tech Stack

- **Pure Python 3** — no dependencies, no npm, no build tools
- **Vanilla HTML/CSS/JS** — no frameworks, loads instantly
- **Google Fonts** (Bebas Neue, Exo 2, JetBrains Mono) — loaded via CDN
- **GitHub Pages** — free hosting, HTTPS included

---

## License

This codebase is provided for your personal affiliate use. AllMyTube is a product of Wondershare. This site is an independent affiliate guide and is not affiliated with or endorsed by Wondershare.
