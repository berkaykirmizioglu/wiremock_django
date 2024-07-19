# Wiremock & Django - Dynamic Mocking App via UI

This project integrates Wiremock with Django to allow for dynamic mocking of APIs through the Django admin interface. 
The project is containerized using Docker for easy setup and deployment.

## Features

- Manage Wiremock stubs through the Django admin panel
- Automatically sync stubs to Wiremock
- Use PostgreSQL as the database
- Containerized with Docker

## Prerequisites

- Python
- Docker
- Docker Compose

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/berkaykirmizioglu/wiremock_django.git
cd wiremock_django
```

Note:
If you don't use your own env, please create a new one and activate it.
```bash
python -m venv env
source env/bin/activate
```

### Step 2: Build and Start the Docker Containers

```bash
docker-compose up --build
```

This will build the Docker images and start the containers for the Django app, PostgreSQL, and Wiremock.

### Step 3: Create Superuser

The `create_superuser` command will be executed automatically when the containers are started.

### Step 4: Access the Django Admin Panel

Open your browser and navigate to:

```plaintext
http://localhost:8000/admin
```

Log in with the superuser credentials. (default: `admin` / `123456`).

### Step 5: Add Wiremock Stubs

1. Navigate to the `Wiremock Stubs` section in the Django admin panel.
2. Click `Add Wiremock Stub`.
3. Fill in the `name`, `request`, and `response` fields. For example:

- **Name:** Test Stub
- **Request:**
  ```json
  {
    "method": "GET",
    "url": "/api/test"
  }
  ```
- **Response:**
  ```json
  {
    "status": 200,
    "body": "{\"message\": \"This is a test response\"}",
    "headers": {
      "Content-Type": "application/json"
    }
  }
  ```

4. Save the stub. It will be automatically synced to Wiremock.

### Step 7: Test the Stub

Send a request to the stubbed endpoint to verify it works as expected:

```bash
curl -X GET http://localhost:8080/api/test
```

You should receive the following response:

```json
{
  "message": "This is a test response"
}
```

## Project Structure

```plaintext
wiremock_project/
├── wiremock/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── create_superuser.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── wiremock_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── manage.py
├── requirements.txt
```

## Notes

- Ensure you have Docker and Docker Compose installed on your machine.
- The `entrypoint.sh` script ensures that the database is ready before running migrations and creating the superuser.


**Happy Mocking!**
