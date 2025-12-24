# Danny Goldberg
Arava
209428713

# 📇 Contact List API – Docker Compose Project

This project is a containerized Contact Management API built with FastAPI, MySQL, and Docker Compose.

It manages a list of contacts and persists the database using Docker volumes, meaning the data remains available even if containers stop or restart.

## 🚀 Features

- REST API with 4 endpoints
- MySQL database running in Docker
- Persistent database using Docker volumes
- Database initialized automatically with sample data
- Fully reproducible using Docker Compose

## 📂 Project Structure

## 📂 Project Structure

    week10_compose/
        .venv/
        app/
            models/
                contact.py
            utils/
                helper_functions.py
            data_interactor.py
            main.py
        sql/
            init.sql
        Dockerfile
        compose.yaml
        requirements.txt
        .env
        .gitignore
        README.md

## 🧠 Contact Model

Each contact contains:
- id
- first_name
- last_name
- phone

## 🐳 Docker & Database Persistence

The MySQL database runs in a dedicated container and stores its data in a Docker volume.  
The database remains intact even if containers are stopped or restarted.

## 🛠️ Setup & Run Instructions

Clone the repository:

git clone https://github.com/DannyG101/week10_compose.git
cd week10_compose

Build and run the project:

docker compose up --build

The API will be available at:
http://localhost:8000

The MySQL database contacts_db is created automatically and initialized with a contacts table containing 4 random contacts.

## 📌 API Endpoints

Get all contacts:
GET /contacts

curl http://localhost:8000/contacts

Add a new contact:
POST /contacts

curl -X POST http://localhost:8000/contacts \
  -H "Content-Type: application/json" \
  -d '{"first_name":"John","last_name":"Doe","phone":"1234567890"}'

Update a contact by ID:
PUT /contacts/{id}

curl -X PUT http://localhost:8000/contacts/1 \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Jane","last_name":"Smith","phone":"0987654321"}'

Delete a contact by ID:
DELETE /contacts/{id}

curl -X DELETE http://localhost:8000/contacts/1

## 🧪 Stopping the Application

docker compose down

To remove containers and delete the database volume:

docker compose down -v
