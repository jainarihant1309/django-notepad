# 📝 Django Notepad README.txt

A simple Django CRUD application for managing notes.

## Features

- Create Note
- View Notes
- Edit Note
- Delete Note
- SQLite Database
- Django Admin
- Docker Support
- Docker Compose Support

---

## Tech Stack

- Python 3
- Django 5
- SQLite
- Docker
- Docker Compose
- Bootstrap 5

---

## Project Structure

```
django-notepad/
│
├── config/
├── notes/
├── templates/
├── static/
├── media/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

---

## Local Setup

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Linux

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py migrate
```

Start Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

## Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

## Admin User

```bash
python manage.py createsuperuser
```

---

## Author

Arihant Jain
