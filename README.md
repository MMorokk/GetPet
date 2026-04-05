# GetPet

A Flask-based web application for showcasing pets available for adoption or sale. Content is configured via Markdown (in `info.toml`) and individual pet data is defined in TOML files.

## Requirements

- Python >= 3.13
- [`uv`](https://github.com/astral-sh/uv) (recommended) or pip

## Setup

```bash
# Install dependencies
uv sync

# Configure environment (optional)
cp .env-example .env
# Edit .env with your details

# Run
python app.py
```

The app runs at `http://localhost:5000` by default.

## Environment Variables

| Variable | Description |
|---|---|
| `WEBSITE_TITLE` | Name shown in the browser tab |
| `CONTACT_ADDRESS` | Address for the contact page |
| `CONTACT_PHONE` | Phone number for the contact page |
| `CONTACT_EMAIL` | Email for the contact page |
| `GEOLOCATION_LATITUDE` | Latitude for map integration |
| `GEOLOCATION_LONGITUDE` | Longitude for map integration |
| `FLASK_ENV` | Set to `development` for debug mode |
| `FLASK_DEBUG` | Set to `1` for hot reload |

## Adding Pets

Create a `.toml` file in the `/pets/` directory following the structure in `example_jeremy.toml`:

```toml
[general]
name = "Jeremy"
type = "dog"
sex = "male"
breed = "Labrador"
price = 500
date_of_birth = "2022-01-15"
description = "A friendly and energetic dog."
character = "Playful, loyal, energetic"

[appearance]
color = "yellow"
size = "large"
```

Pet images go in `/pets/images/`.

## What Works

| Feature | Status |
|---|---|
| Home page | Working — loads content from `info.toml`, renders Markdown |
| About page | Working — loads content from `info.toml`, renders Markdown |
| Navigation | Working — responsive header with mobile sidebar |
| Dark/light theme | Working — toggles with persistence via `localStorage` |
| TOML pet data loading | Working — `load_pets_from_directory()` parses pet files correctly |
| Responsive design | Working — mobile breakpoint at 700px, fluid typography |

## What Doesn't Work

| Feature | Issue |
|---|---|
| Pets page (`/pets`) | Template is an empty placeholder; `load_pets_from_directory()` is never called in `app.py`; `pets.css` is empty |
| Contact page (`/contact`) | Stub only — contains no form, no map, and no contact info display; POST handler redirects without processing anything |
| Environment variables in templates | The context processor in `app.py` is commented out, so `WEBSITE_TITLE` and contact info from `.env` are never injected into templates |
| Error handling in `loaders.py` | `sys.exit()` is called on errors but `sys` is never imported — will raise `NameError` |

## Known Minor Issues

- Navigation bar contains a leftover debug element (rose-colored "DEBUG" box in `layout.html`).
- `datetime` is imported but unused in `loaders.py`.
- `MarkupSafe` import is commented out in `app.py`.

## Project Structure

```
GetPet/
├── app.py              # Flask routes and application setup
├── loaders.py          # Pet class and TOML loading functions
├── info.toml           # Content for home, about, and contact pages
├── pyproject.toml      # Project metadata and dependencies
├── .env                # Environment variables (not committed)
├── .env-example        # Template for .env
├── pets/               # Pet TOML data files
│   └── example_jeremy.toml
├── templates/
│   ├── layout.html     # Base template (nav, theme toggle, footer)
│   ├── index.html      # Home page
│   ├── about.html      # About page
│   ├── pets.html       # Pet listing page (incomplete)
│   └── contact.html    # Contact page (stub)
└── static/
    ├── base.css        # Global styles (Rose Pine theme, responsive layout)
    ├── base.js         # Mobile sidebar behaviour
    ├── theme.js        # Dark/light theme toggle
    ├── index.css       # Home page styles
    ├── about.css       # About page styles
    ├── pets.css        # Pet listing styles (empty)
    └── imgs/
        └── 1.jpg       # Background image used on home and about pages
```
