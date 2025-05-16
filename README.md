# 🚀 Employee Management System

A full-stack Employee Management app with **FastAPI** backend and **Next.js + TypeScript** frontend, using **MySQL** database.

---

## ✨ Features

- CRUD operations on employee records
- FastAPI + SQLAlchemy backend
- Next.js + React + TypeScript frontend
- MySQL for persistent storage
- CORS enabled for API communication
- Clean, modular, and extendable codebase

---

## 🛠️ Tech Stack

| Backend          | Frontend             | Database    |
| ---------------- | -------------------- | ----------- |
| Python 3.9+      | Next.js (React + TS) | MySQL       |
| FastAPI          | Axios                | SQLAlchemy  |
| SQLAlchemy ORM   |                      |             |

---

## 🚀 Getting Started

# Prerequisites

- Python 3.9+
- Node.js 18+
- MySQL Server

## Backend Setup

## Clone repo and go to backend folder
python -m venv venv
## Activate virtual environment
## Linux/macOS
source venv/bin/activate
## Windows
venv\Scripts\activate

pip install fastapi uvicorn sqlalchemy mysql-connector-python

## Configure database connection in database.py
### DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/employees"

uvicorn main:app --reload



## Frontend Setup

This project uses **Next.js** with **TypeScript** and **Axios** for API requests.

### 1. Create Next.js + TypeScript App (if not created)

npx create-next-app@latest frontend --typescript


### 2. Navigate to the frontend folder
      cd frontend
### 3. Install Axios
   npm install axios


### 4. Create a simple Employee form
In src/pages/index.tsx (or src/app/page.tsx for Next.js 13+), add:

### 5. Run frontend server
   npm run dev



## 🔗 API Endpoints

| Method | Endpoint          | Description           |
| ------ | ----------------- | --------------------- |
| POST   | `/employees/`     | Create new employee   |
| GET    | `/employees/`     | Get all employees     |
| PUT    | `/employees/{id}` | Update employee by ID |
| DELETE | `/employees/{id}` | Delete employee by ID |


## 🧪 Postman Test Cases

| Operation         | Method | URL               | Body (JSON)                                     | Expected Response                       |
| ----------------- | ------ | ----------------- | ----------------------------------------------- | --------------------------------------- |
| Create Employee   | POST   | `/employees/`     | `{ "name": "Alice", "location": "NY" }`         | Employee object with id, name, location |
| Get All Employees | GET    | `/employees/`     | None                                            | Array of employee objects               |
| Update Employee   | PUT    | `/employees/{id}` | `{ "name": "Alice Updated", "location": "SF" }` | Updated employee object                 |
| Delete Employee   | DELETE | `/employees/{id}` | None                                            | `{ "detail": "Deleted" }`               |


## 🚀 Future Improvements
Add user authentication & authorization

Frontend form validation and notifications

Pagination and search/filter functionality

Dockerize backend and frontend

Unit and integration tests
