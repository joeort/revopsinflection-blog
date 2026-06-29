# RevOps Unfiltered — Blog Archive

Joe Ort's Substack posts on revenue operations, GTM strategy, and B2B SaaS operations.

## Overview

This repository contains:
- **35+ blog posts** from RevOps Unfiltered (Substack)
- **Automated weekly sync** via GitHub Actions
- **Full-text search** via the INDEX.md

## Automation

A GitHub Actions workflow runs every Monday at 9am UTC to automatically fetch new posts from the Substack RSS feed and commit them to this repo. You can also trigger the sync manually.

**Trigger manually:** Go to Actions → Sync Substack Posts → Run workflow

## Files

- `sync.py` — Python script that fetches Substack RSS, converts HTML to markdown, and updates INDEX.md
- `.github/workflows/sync.yml` — GitHub Actions workflow configuration
- `INDEX.md` — Master index of all posts with summaries
- `*.md` — Individual post files (YYYY-MM-DD-slug.md)

## Local Usage

Clone this repo and pull anytime to get the latest posts:

```bash
git clone https://github.com/joeort/revopsinflection-blog.git
cd revopsinflection-blog
git pull
```

To manually run the sync script locally:

```bash
pip install html2text python-dateutil
python sync.py
```
