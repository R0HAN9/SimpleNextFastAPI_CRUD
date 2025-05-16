# Employee Management System

A simple full-stack Employee Management application built with **FastAPI** (backend) and **Next.js + TypeScript** (frontend), using **MySQL** as the database.

---

## Features

- **Create**, **Read**, **Update**, and **Delete** (CRUD) employee records.
- Backend REST API built with FastAPI and SQLAlchemy for efficient database operations.
- Frontend built with Next.js using React and TypeScript for a modern, type-safe user interface.
- MySQL database for persistent and reliable data storage.
- CORS configured for smooth frontend-backend communication.
- Easy-to-understand code structure with clear separation of concerns.
- Ready for extension with additional features like authentication and pagination.

---

## Tech Stack

| Backend          | Frontend             | Database    |
|------------------|----------------------|-------------|
| Python 3.9+      | Next.js (React + TS) | MySQL       |
| FastAPI          | Axios (HTTP client)  | SQLAlchemy  |
| SQLAlchemy ORM   |                      |             |

---

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- MySQL Server

### Backend Setup

1. Clone the repository and navigate to the backend folder.

2. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows

3. Install dependencies:

pip install fastapi uvicorn sqlalchemy mysql-connector-python

4. Configure your MySQL connection in database.py:

DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/employees"


5. Start the backend server:
uvicorn main:app --reload


Frontend Setup
Navigate to the frontend folder.

Install dependencies:
npm install

Run the frontend development server:
npm run dev
Open http://localhost:3000 in your browser.

API Endpoints

| Method | Endpoint          | Description           |
| ------ | ----------------- | --------------------- |
| POST   | `/employees/`     | Create new employee   |
| GET    | `/employees/`     | Get all employees     |
| PUT    | `/employees/{id}` | Update employee by ID |
| DELETE | `/employees/{id}` | Delete employee by ID |


Postman Test Cases
You can use Postman to test all CRUD operations as follows:

| Operation         | Method | URL               | Body (JSON)                                     | Expected Response                       |
| ----------------- | ------ | ----------------- | ----------------------------------------------- | --------------------------------------- |
| Create Employee   | POST   | `/employees/`     | `{ "name": "Alice", "location": "NY" }`         | Employee object with id, name, location |
| Get All Employees | GET    | `/employees/`     | None                                            | Array of employee objects               |
| Update Employee   | PUT    | `/employees/{id}` | `{ "name": "Alice Updated", "location": "SF" }` | Updated employee object                 |
| Delete Employee   | DELETE | `/employees/{id}` | None                                            | `{ "detail": "Deleted" }`               |


Future Improvements
Add user authentication and authorization.

Implement frontend form validation and notifications.
Add pagination and search/filter capabilities.
Dockerize backend and frontend for easy deployment.
Add unit and integration tests.
