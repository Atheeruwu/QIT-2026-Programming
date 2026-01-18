# QIT-2026-Programming

Django project for QIT 2026 Programming course with multi-student structure.

## Repository Structure

```
repo/
├── manage.py
├── requirements.txt
├── core/                  # Django project (DO NOT TOUCH)
│   ├── settings.py
│   ├── urls.py
│   ├── views.py           # Global index view
│   └── ...
├── sections/              # Individual student sections
│   ├── juan_pablo/
│   │   ├── views.py
│   │   └── urls.py
│   ├── cesar/
│   │   ├── views.py
│   │   └── urls.py
│   ├── atheer/
│   │   ├── views.py
│   │   └── urls.py
│   ├── emmanuel/
│   │   ├── views.py
│   │   └── urls.py
│   ├── praneet/
│   │   ├── views.py
│   │   └── urls.py
│   └── frankie/
│       ├── views.py
│       └── urls.py
└── README.md
```

## Navigation Structure

The project follows a three-level navigation structure:

1. **Global Index** (`/`) - Displays the names of all students
2. **Student Index** (`/student_name/`) - Displays the three applications implemented by that student
3. **Application View** (`/student_name/app1/`, etc.) - Displays the selected application

## Strict Rules

### ❌ You must NOT modify:
- `manage.py`
- `core/settings.py`
- `core/urls.py` (except for adding your own section route)
- Folders belonging to other students
- `requirements.txt` (unless absolutely necessary)

### ✅ You must:
- Work only inside `sections/your_name/`
- Keep your code isolated
- Ensure that the Django server starts successfully

⚠️ **If your code prevents Django from starting, the entire project fails, and this will negatively affect your evaluation.**

## Student Sections

Each student must implement their section at `/student_name/` with:
- A section index displaying the student's full name
- Exactly three links, one for each assigned application:
  - Application 1: LeetCode problem
  - Application 2: Syllabus assignment (to be shared)
  - Application 3: Basic quantum gates simulator

## How to Run the Project Locally

From the root of the repository:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## Example Implementation

Each student section should have a `views.py` and `urls.py` file. Example structure:

**views.py:**
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>Your Name</h1>
        <ul>
            <li><a href="app1/">Application 1</a></li>
            <li><a href="app2/">Application 2</a></li>
            <li><a href="app3/">Application 3</a></li>
        </ul>
    """)

def app1(request):
    return HttpResponse("Application 1")

def app2(request):
    return HttpResponse("Application 2")

def app3(request):
    return HttpResponse("Application 3")
```

**urls.py:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("app1/", views.app1, name="app1"),
    path("app2/", views.app2, name="app2"),
    path("app3/", views.app3, name="app3"),
]
```

(Using templates instead of HttpResponse is allowed and encouraged, but not required.)

## What is NOT Required

- Database
- Models
- Migrations
- Authentication
- Advanced frontend (CSS/JS frameworks)

This project focuses on structure, routing, and understanding Django fundamentals.

## Important Final Rule

**"It works on my machine" is not sufficient.**

Your code must work within the shared project, without breaking other people's work. This is a core part of the exercise.
