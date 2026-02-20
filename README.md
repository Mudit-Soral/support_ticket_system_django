# Django Support Ticket System

A full-featured Support Ticket System built with Django. This project allows users to create, manage, assign, and track support tickets with authentication and role-based access.

---

## Features

* User authentication (Login / Logout)
* Create support tickets
* Edit and delete tickets
* Assign tickets to staff users
* Track ticket progress (0–100%)
* Ticket status management:

  * Open
  * In Progress
  * Resolved
  * Closed
* View ticket details
* Staff-only assignment system
* Clean and structured backend using Django best practices

---

## Tech Stack

* Python
* Django
* SQLite
* HTML
* CSS (basic)
* Git & GitHub

---

## Project Structure

```
support_ticket_system/
│
├── support_ticket_system_main/
│   ├── support_ticket/
│   ├── tickets/
│   ├── manage.py
│   └── db.sqlite3
│
├── venv/
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/python-django-support-ticket-system.git
```

Go into the project:

```
cd python-django-support-ticket-system
```

Create virtual environment:

```
python -m venv venv
```

Activate virtual environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install django
```

Run migrations:

```
python manage.py migrate
```

Create superuser:

```
python manage.py createsuperuser
```

Run server:

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000
```

---

## Author

Built by Mudit Soral

---

## Future Improvements

* Email notifications
* File attachments
* User registration
* Dashboard analytics
* REST API support
* Deployment to cloud

---

## License

This project is open source and free to use.
