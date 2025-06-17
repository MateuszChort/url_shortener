# 🔗 Minimalist URL Shortener API (Django + DRF)

A lightweight API-only project that lets you shorten and expand URLs, similar to [tinyurl.com](https://tinyurl.com), built with Django and Django REST Framework.

---

## 🚀 Features

- Shorten long URLs (e.g., `http://example.com/very/long/url`)
- Expand shortened URLs back to the original
- Admin panel available
- Interactive API docs via Swagger (drf-spectacular)
- Pytest-based test suite

---

## 🛠️ Setup Instructions

### 1. Clone and set up the environment

```bash
git clone <repository-url>
cd url_shortener
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Create a superuser (to access Django Admin)

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

---

## 📚 API Documentation

Once the server is running, visit:

> **Swagger UI**: [http://localhost:8000/schema/swagger/](http://localhost:8000/schema/swagger/)

You can use it to:
- Test the POST `/shorten/` endpoint to generate short URLs
- Test the GET `/short/{code}/` endpoint to expand them

---

## 🔒 Django Admin

Log into the Django admin interface at:

> [http://localhost:8000/admin/](http://localhost:8000/admin/)

Use the superuser credentials you created earlier. You can view and manage stored URLs here.

---

## ✅ Running Tests

This project uses **pytest** and **pytest-django**.

To run tests:

```bash
pytest
```

Tests use `pytest-mock` to mock short code generation and verify behavior.

---

## 📦 Requirements

Minimal dependencies are defined in `requirements.txt`:


## 📌 Notes

- URL codes are randomly generated and 6 characters long
- You cannot duplicate URL

---

## 📮 License

MIT – free to use, modify and distribute.