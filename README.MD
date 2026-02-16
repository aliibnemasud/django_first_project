## Django Project

Simple Django project with a single app (`myapp`) that serves a few basic routes and a static `about` page.

### Features

- Basic routes: home, profile, settings, about
- Template rendering for the about page
- Static CSS for the about page

### Requirements

- Python 3.10+ (recommended)
- Django 6.0.2

### Setup

1. Create and activate a virtual environment
2. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the server

```bash
python manage.py runserver
```

### Useful URLs

- Home: `http://127.0.0.1:8000/`
- About: `http://127.0.0.1:8000/about/`

### Project Structure

- `config/` - Django project settings and URLs
- `myapp/` - Main app views, urls, templates, and static files
- `db.sqlite3` - Local development database (ignored in git)
