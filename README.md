# To-Do List (Django)

A minimal server-rendered To-Do app built with Django. No REST or frontend framework — just Django views, templates, and a small static CSS file.

## Features
- List all tasks
- Add a new task
- Mark a task as done
- Delete a task
- Simple, secure forms with CSRF protection

## Tech Stack
- Django 6
- SQLite (default)

## Project Layout
```
To-do-List/
  backend/
    backend2/            # Django project (settings, urls)
    tasks/               # App (models, views, urls)
    templates/           # Django templates
      tasks/
        list.html
    static/
      tasks.css          # Styles for the list page
    manage.py
    requirements.txt
    .env                 # Your local secrets (not committed)
    .env.example         # Template for required env vars
  virtualenv/            # Local Python venv (optional location)
  public/                # Legacy static page (not used now)
```

## Prerequisites
- Python 3.10+ installed and on PATH

## Setup (Windows, cmd.exe)
```cmd
cd "a:\\VS CODE\\Projects\\To-do-List"
python -m venv virtualenv
virtualenv\Scripts\activate
cd backend
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000/ in your browser.

## Environment Variables
Configured via `backend/.env` (example in `backend/.env.example`).
- `SECRET_KEY`: Django secret key (use a unique value for prod)
- `DEBUG`: `True` or `False`
- `ALLOWED_HOSTS`: Comma-separated list (e.g., `localhost,127.0.0.1`)

## How It Works
- URL routing:
  - `/` → tasks list page
  - `/add/` → POST to add a task
  - `/done/<id>/` → POST to mark as done
  - `/delete/<id>/` → POST to delete
- Views: Plain Django views in `backend/tasks/views.py`
- Template: `backend/templates/tasks/list.html`
- Styles: `backend/static/tasks.css`

## Common Commands
```cmd
REM From the backend folder
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
```

## Notes
- The `public/` folder is not used in this server-rendered version.
- If you later want a separate frontend or REST API, you can reintroduce DRF and CORS as needed.
