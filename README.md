# SkillXchange API

Welcome to the SkillXchange API, a platform designed for users to enroll in courses, leave reviews, and manage user roles such as Admin, Tutor, and Student.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Admin Interface](#admin-interface)
- [Contributing](#contributing)
- [License](#license)

## Features
- User management with role-based access (Admin, Tutor, Student)
- Course management including creation, update, and deletion
- Enrollment management to keep track of students in courses
- Review system for students to rate and comment on courses
- API documentation with Swagger and ReDoc

## Technologies Used
- **Django**: A high-level Python web framework for rapid development.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **Django Filter**: To enable filtering on querysets.
- **DRF YASG**: For generating interactive API documentation.
- **SQLite**: Default database for development (can be replaced with others).

## Installation
Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anageguchadze/SkillXchange---Community-Skill-Sharing-Platform
   cd skillxchange

2. Create a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
bash
pip install -r requirements.txt

4.Run database migrations:
bash
python manage.py migrate

5. Create a superuser (optional but recommended for admin access):
bash
python manage.py createsuperuser

6. Run the development server:
bash
python manage.py runserver
Your API should now be running at http://127.0.0.1:8000/api/.

Usage
API Endpoints
Users: /api/users/
Courses: /api/courses/
Enrollments: /api/enrollments/
Reviews: /api/reviews/
Example API Requests

Get all courses:
bash
curl -X GET http://127.0.0.1:8000/api/courses/

Create a new course:
bash
curl -X POST http://127.0.0.1:8000/api/courses/ -H "Content-Type: application/json" -d '{"title": "Course Title", "description": "Course Description", "tutor": 1, "start_date": "2024-01-01", "end_date": "2024-12-31", "max_students": 30}'
API Documentation

The API documentation is automatically generated and can be accessed through the following URLs:
Swagger UI
ReDoc
Admin Interface
Access the Django admin interface at http://127.0.0.1:8000/admin/. Log in using the superuser credentials you created during the installation.

Contributing
We welcome contributions to the SkillXchange API! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes.
Push your branch and create a pull request.
License
This project is licensed under the BSD License - see the LICENSE file for details.

Thank you for checking out the SkillXchange API! For further questions or issues, feel free to reach out.

markdown

### Instructions for Customization:
- **GitHub URL**: Replace `https://github.com/yourusername/skillxchange.git` with the actual URL of your repository.
- **License**: Ensure that the licensing section matches your project's license.
- **API Requests**: Adjust example requests to fit your actual model and data formats if necessary.
- **Features**: You can expand or modify the features section based on what your project offers.

Feel free to ask if you need further adjustments or additional sections!






