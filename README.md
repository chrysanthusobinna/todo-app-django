# Django Todo App

## Overview

This is a simple Todo application built with Django. It allows users to create, view, edit, and delete todo items. The application includes features to manage tasks efficiently and is a great example of a basic CRUD (Create, Read, Update, Delete) application using Django.

## Features

- **Create Todo Items**: Add new tasks to your todo list.
- **View Todo Items**: Display a list of all tasks.
- **Edit Todo Items**: Modify existing tasks.
- **Delete Todo Items**: Remove tasks from your list.
- **Mark Tasks as Complete**: Update task status to completed.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default in Django)
- **Version Control**: Git and GitHub

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (recommended for isolating dependencies)

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/django-todo-app.git
    cd django-todo-app
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (for admin access)**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

7. **Access the Application**

    Open your web browser and navigate to `http://localhost:8000` to view the todo app. For the admin interface, go to `http://localhost:8000/admin` and log in with the superuser credentials.

## Usage

- **Add a New Todo**: Use the provided form to add new tasks to the list.
- **Edit a Todo**: Click on the edit button next to a task to modify it.
- **Delete a Todo**: Use the delete button to remove tasks.
- **Mark as Complete**: Toggle the completion status of tasks as needed.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a Pull Request.

 
## Contact

For any questions or suggestions, please reach out to the project maintainer:

- **Name**: Chrysanthus Chiagwah
- **Email**: chrysanthusobinna@gmail.com

