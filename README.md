# Employee Search Microservice (Django REST Framework)

This is a backend-only microservice built using **Django** and **Django REST Framework** to provide a scalable, organization-configurable **employee search API** for HR systems.

---

## Features

- Search employees by name, filters like location, status, department, position, and company.
- Dynamic organization-specific columns based on configuration.
- In-memory rate limiting (no external library).
- Unit-tested using `pytest` and `pytest-django`.
- Dockerized for isolated development.
- OpenAPI (minimal schema endpoint only, no UI).
- No external libraries used for business logic or rate limiting.

---

## Technologies

- Python 3.12+
- Django 4.x
- Django REST Framework
- Pytest (with pytest-django)
- Docker

---

# Build the Docker image
docker build -t employee-search .

# Run the container
docker run -p 8000:8000 employee-search