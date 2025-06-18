# Clinic Appointment Management System

## Purpose

This project is a simple clinic appointment management system built with Django. It allows patients to make appointments with their chosen or preferred doctor. The system records the patient's arrival time under each appointment and tracks which consultation room was used. Administrators can check available rooms, and doctors can book a room in advance.

## Technologies Used

- Django (Python web framework)
- Bootstrap (for frontend styling)
- SQLite (default database, but you can use MySQL or any database supported by Django ORM)
- `requests` Python package (for country API integration)

## Installation & Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies**:
    ```sh
    pip install django requests
    ```

3. **Create a new Django project** (if you haven't already):
    ```sh
    django-admin startproject your_project_name .
    cd your_project_name
    ```

4. **Add the apps to your project**:
    - Copy or move the `appointment`, `doctor`, and `patients` apps into your project directory.
    - In your `settings.py`, add these apps to the `INSTALLED_APPS` list:
        ```python
        INSTALLED_APPS = [
            # ...existing apps...
            'appointment',
            'doctor',
            'patients',
        ]
        ```

5. **Configure templates and static files** in `settings.py`:
    ```python
    TEMPLATES = [
        {
            # ...existing config...
            'DIRS': [BASE_DIR / 'templates'],
            # ...existing config...
        },
    ]
    STATICFILES_DIRS = [BASE_DIR / 'static']
    ```

6. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

8. **Access the application** at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Notes

- You can switch to MySQL or another database by updating the `DATABASES` setting in `settings.py`.
- Make sure to install any additional dependencies as needed.

---