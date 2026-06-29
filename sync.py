#!/usr/bin/env python3
"""
Sync Substack posts to local markdown files.
- Fetches RSS feed, parses full HTML content
- Writes new posts to blog/ folder with frontmatter
- Updates INDEX.md with new entries
- Idempotent: only creates files for posts not yet in the folder
"""

import xml.etree.ElementTree as ET
import os
import re
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request

try:
    import html2text
except ImportError:
    print("ERROR: html2text not installed. Run: pip install html2text python-dateutil")
    exit(1)

FEED_URL = "https://revopsinflection.substack.com/feed"
BLOG_DIR = Path(__file__).parent
INDEX_FILE = BLOG_DIR / "INDEX.md"

# Namespaces
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "atom": "http://www.w3.org/2005/Atom",
}

def fetch_feed():
    """Fetch RSS feed XML."""
    print(f"Fetching {FEED_URL}...")
    req = Request(FEED_URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    with urlopen(req) as response:
        return response.read().decode("utf-8")

def parse_feed(xml_text):
    """Parse RSS feed and return list of posts."""
    root = ET.fromstring(xml_text)
    posts = []

    for item in root.findall(".//item"):
        title_elem = item.find("title")
        link_elem = item.find("link")
        pub_date_elem = item.find("pubDate")
        content_elem = item.find("content:encoded", NS)

        if not all([title_elem is not None, link_elem is not None, pub_date_elem is not None, content_elem is not None]):
            continue

        title = title_elem.text or ""
        link = link_elem.text or ""
        pub_date_str = pub_date_elem.text or ""
        html_content = content_elem.text or ""

        # Parse date: "Mon, 26 Jun 2026 00:00:00 GMT" -> "2026-06-26"
        try:
            date_obj = datetime.strptime(pub_date_str.replace(" GMT", ""), "%a, %d %b %Y %H:%M:%S")
            date_str = date_obj.strftime("%Y-%m-%d")
        except Exception as e:
            print(f"  WARNING: Could not parse date '{pub_date_str}': {e}")
            continue

        posts.append({
            "title": title,
            "url": link,
            "date": date_str,
            "html": html_content,
        })

    return posts

def slugify_url(url):
    """Extract slug from Substack URL."""
    # URL pattern: https://revopsinflection.substack.com/p/{slug}
    match = re.search(r"/p/([a-z0-9-]+)", url)
    return match.group(1) if match else "unknown"

def file_exists(date_str, slug):
    """Check if a post file already exists."""
    filename = f"{date_str}-{slug}.md"
    return (BLOG_DIR / filename).exists()

def html_to_markdown(html_text):
    """Convert HTML to markdown."""
    h = html2text.HTML2Text()
    h.body_width = 0  # Don't wrap lines
    h.ignore_links = False
    h.ignore_images = False
    return h.handle(html_text).strip()

def write_post(date_str, slug, title, url, markdown_content):
    """Write post to file with frontmatter."""
    filename = f"{date_str}-{slug}.md"
    filepath = BLOG_DIR / filename

    frontmatter = f"""---
title: "{title.replace('"', '\\"')}"
date: {date_str}
url: {url}
---

"""

    filepath.write_text(frontmatter + markdown_content, encoding="utf-8")
    print(f"  Created: {filename}")
    return filename

def read_index():
    """Read INDEX.md and extract existing entries."""
    if not INDEX_FILE.exists():
        return []

    content = INDEX_FILE.read_text(encoding="utf-8")
    # Look for markdown links: [title](./YYYY-MM-DD-slug.md)
    pattern = r"\]\(\./([\d]{4}-[\d]{2}-[\d]{2}-[a-z0-9-]+\.md)\)"
    return re.findall(pattern, content)

def add_to_index(date_str, slug, title, url):
    """Prepend new entry to INDEX.md (below header)."""
    filename = f"{date_str}-{slug}.md"

    # Read existing content
    existing = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""

    # Find where to insert (after the closing ---, before first real entry)
    sep_match = re.search(r"^---\s*\n", existing, re.MULTILINE)
    if sep_match:
        insert_pos = sep_match.end()
    else:
        insert_pos = existing.find("\n\n") + 2

    new_entry = f"""
## [{title}]({url})
_{date_str}_ · [`{filename}`](./{filename})

"""

    updated = existing[:insert_pos] + new_entry + existing[insert_pos:]

    # Update post count in header
    match = re.search(r"_(\d+) posts", updated)
    if match:
        old_count = int(match.group(1))
        new_count = old_count + 1
        updated = re.sub(r"_\d+ posts", f"_{new_count} posts", updated, count=1)

    INDEX_FILE.write_text(updated, encoding="utf-8")
    print(f"  Updated INDEX.md")

def main():
    print("Starting Substack sync...\n")

    # Fetch and parse feed
    xml_text = fetch_feed()
    posts = parse_feed(xml_text)
    print(f"Found {len(posts)} posts in feed.\n")

    existing_files = read_index()
    new_count = 0

    for post in posts:
        slug = slugify_url(post["url"])
        date = post["date"]

        if file_exists(date, slug):
            print(f"  Skipped: {date}-{slug}.md (already exists)")
            continue

        print(f"Processing: {post['title']} ({date})")
        markdown = html_to_markdown(post["html"])
        write_post(date, slug, post["title"], post["url"], markdown)
        add_to_index(date, slug, post["title"], post["url"])
        new_count += 1

    print(f"\nSync complete. {new_count} new post(s) added.")

if __name__ == "__main__":
    main()
