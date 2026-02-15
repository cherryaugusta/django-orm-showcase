# Enterprise Django ORM Showcase

**Django 5.x · Python 3.12+**

This repository demonstrates advanced Django ORM capabilities:

- Custom managers
- Service layer abstraction
- Indexed queries
- Transactional integrity
- Test-driven development
- Enterprise-level folder structure

## Installation

1. Clone the repository:

```
git clone https://github.com/cherryaugusta/enterprise-django-orm-showcase.git
cd enterprise-django-orm-showcase
```

2. Create and activate virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate # Windows
   ```

# source venv/bin/activate # macOS / Linux

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   cd sample
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run development server:
   ```
   python manage.py runserver
   ```
   Visit:
   ```
   http://127.0.0.1:8000/
   ```

---

## Folder Structure

django-orm-showcase/
├── sample/
│ ├── manage.py
│ ├── sample/
│ │ └── settings/
│ └── cuisine/
│ ├── managers.py
│ ├── models.py
│ ├── services.py
│ ├── admin.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ │ └── cuisine/
│ │ ├── cuisine_list.html
│ │ └── cuisine_detail.html
│ └── tests/
├── requirements.txt
├── .gitignore
├── README.md
├── .env.example
├── staticfiles/
├── media/
├── venv/
├── .vscode/
└── .idea/

---

## Notes

• staticfiles/ → collect static files for production.
• media/ → store uploaded files like images.
• .env.example → copy to .env and fill in secret values.
• venv/ → virtual environment (excluded from Git).
• .vscode/ and .idea/ → IDE configs (ignored in Git).

---

## License

MIT License

---
