# Todos API

A simple API for managing todos, categories, and users using Django REST Framework. Developed as part of the Django Advanced course workshop at Software University.

## Features

- **Todos Management**:
  - Create and retrieve todos via the API.
  - Update todos (e.g., `PUT /api/todos/<id>/`).
  - **Delete functionality for todos is not implemented** based on the current implementation.

- **Categories Management**:
  - Read-only access to categories:
    - Categories can only be listed (`GET /api/todos/categories/`).
    - Categories cannot be created, updated, or deleted through the API.

- **Authentication and Authorization**:
  - Powered by Django and SimpleJWT for secure user authentication.

- **Interactive API Documentation**:
  - Integrated with Swagger UI and ReDoc for a user-friendly API exploration experience.

- **Extensible and Modular Architecture**:
  - Designed for seamless integration of additional features and updates.

---

### Todos Management

- **Endpoints**:
  - `GET /api/todos/`: List all todos, with optional filters by category and completion state.
  - `POST /api/todos/`: Create a new todo item.
  - `GET /api/todos/<id>/`: Retrieve details of a specific todo item by ID.
  - `PUT /api/todos/<id>/`: Update an existing todo item by ID.

- **Key Features**:
  - Filter todos by category and completion state using query parameters.
  - Assign multiple users to a todo item for collaboration.

- **Limitations**:
  - Delete functionality for todos is not implemented.

---

### Categories Management

- **Endpoints**:
  - `GET /api/todos/categories/`: Retrieve a list of all categories.

- **Key Features**:
  - Provides read-only access to categories.

- **Limitations**:
  - Categories cannot be created, updated, or deleted through the API.

---

### User Management

- **Endpoints**:
  - `POST /auth/register/`: Register a new user.
  - `POST /auth/login/`: Authenticate a user and retrieve JWT tokens.
  - `POST /auth/logout/`: Revoke a user's refresh token.

- **Authentication**:
  - Secure authentication using JSON Web Tokens (JWT).
  - Integration with `rest_framework_simplejwt` for token-based authentication.

---

### API Documentation

- Schema generated using [drf-spectacular](https://github.com/tfranzel/drf-spectacular).
- Available at:
  - Swagger UI: [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
  - ReDoc: [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)

---

## Installation Instructions

### Prerequisites

- Python 3.11 or higher.
- PostgreSQL or SQLite for database support.

### Steps to Set Up

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment**:
   - For macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Create a PostgreSQL database:
     ```sql
     CREATE DATABASE <database_name>;
     ```
   - Add your database credentials to the `.env` file:
     ```plaintext
     SECRET_KEY=<your_django_secret_key>
     DB_NAME=<database_name>
     DB_USER=<username>
     DB_PASSWORD=<password>
     DB_HOST=localhost
     DB_PORT=5432
     ```

5. **Run Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## Accessing the Application

### API Endpoints

| Method | Endpoint                  | Description                       |
|--------|---------------------------|-----------------------------------|
| GET    | `/api/todos/`             | List all todos with filters.     |
| POST   | `/api/todos/`             | Create a new todo item.          |
| GET    | `/api/todos/<id>/`        | Retrieve a specific todo by ID.  |
| PUT    | `/api/todos/<id>/`        | Update a specific todo by ID.    |
| GET    | `/api/todos/categories/`  | List all categories.             |
| POST   | `/auth/register/`         | Register a new user.             |
| POST   | `/auth/login/`            | Login and retrieve JWT tokens.   |
| POST   | `/auth/logout/`           | Logout and blacklist refresh token. |

### Interactive Documentation

- Explore the API using:
  - Swagger UI: [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
  - ReDoc: [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)


---

### Notes on API Schema Integration

The application uses **drf-spectacular** for API schema generation, ensuring comprehensive documentation and ease of client integration.

---