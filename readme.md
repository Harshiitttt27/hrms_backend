### HRMS Lite – Django Backend
## Overview

HRMS Lite is a lightweight Human Resource Management System designed to manage employees and track daily attendance.
This backend is built with Django and PostgreSQL, exposing RESTful APIs for all functionality.

The system supports:

> Employee management (add, list, delete)

> Attendance tracking (mark present/absent, view records)

> Validation and duplicate prevention

> Consistent API response structure

## Features
> Employee Management

> Add a new employee with employee_id, full_name, email, and department

> List all employees with count and messages

> Delete an employee with success/error message

## Server-side validation:

> Required fields

> Unique email and employee ID

> Proper HTTP status codes and messages

> Attendance Management

> Mark attendance for an employee (Present / Absent) using employee_id

> View attendance records for a specific employee

> Prevent duplicate attendance for the same date

> Return formatted dates (YYYY-MM-DD) and consistent API response

## Tech Stack

> Backend: Python, Django 6

> Database: PostgreSQL

> API: Django REST Framework

> Environment Management: venv

## Project Structure
```
hrms_backend/
│
├── employees/          # Employee app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── attendance/         # Attendance app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── hrms/               # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
|___.env
├── requirements.txt
└── README.md
```
## Installation and local setup
## 1. Clone the repository 
```
git clone <your-repo-url>
cd hrms_backend
```
## 2. Create a virtual environment 
```
python -m venv env
```
## 3. Activate the virtual environment 
> windows CMD
```
.\env\Scripts\activate.bat
```
> Linux/Mac
```
source env/bin/activate
```
## 4. Install Dependencies
```
pip install -r requirements.txt
```
## 5. Create environment variables (.env file)
```
SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=hrms_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```
## Update settings.py to use env variables 
```
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}
```
## Database Setup
> Create postgreeSQL Database
```
CREATE DATABASE hrms_db;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
GRANT ALL PRIVILEGES ON DATABASE hrms_db TO your_db_user;
```
> Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
## Run Server
```
python manage.py runserver
```
Server will start at http://127.0.0.1:8000/

## API Endpoints
> Employees

| Method | Endpoint                        | Description        |
| ------ | ------------------------------- | ------------------ |
| GET    | `/api/employees/`               | List all employees |
| POST   | `/api/employees/`               | Add new employee   |
| DELETE | `/api/employees/<employee_id>/` | Delete employee    |


> Attendance

| Method | Endpoint                         | Description                           |
| ------ | -------------------------------- | ------------------------------------- |
| POST   | `/api/attendance/`               | Mark attendance using `employee_id`   |
| GET    | `/api/attendance/<employee_id>/` | Get attendance records of an employee |

## Validation & Error Handling

> Required fields must be present

> Email must be valid and unique

> Employee ID must be unique

> Attendance duplicates prevented

> Proper HTTP status codes: 200, 201, 400, 404

## License
This project is open-source and free to use.



