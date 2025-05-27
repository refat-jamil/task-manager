# 📝 Task Manager - Django Project

This is a simple Task Manager web application built using **Django** and **Django REST Framework**.  
It allows users to register, log in, and manage their daily tasks efficiently.

---

## 🚀 Features

- User registration and login
- Create, update, and delete tasks
- Mark tasks as completed
- API powered by Django REST Framework
- Secured with user authentication
- Responsive admin panel

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (for development)
- Git & GitHub

---

## 📸 Screenshots



---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```


2. **Create virtual environment**

```bash

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Migrations**
```bash
python manage.py migrate
```

5. **Create superuser (admin)**
```bash
python manage.py createsuperuser
```

6. **Start the development server**
```bash
python manage.py runserver

```

## 🔑 API Endpoints

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | `/api/tasks/`      | List all tasks    |
| POST   | `/api/tasks/`      | Create a new task |
| PUT    | `/api/tasks/<id>/` | Update a task     |
| DELETE | `/api/tasks/<id>/` | Delete a task     |

## ✅ To Do (Future Features)
- JWT Authentication

- Frontend with HTML/CSS or React

- Due date & reminders

- Task categories

