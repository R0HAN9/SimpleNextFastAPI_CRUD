from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employees/", response_model=list[schemas.EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

@app.put("/employees/{id}", response_model=schemas.EmployeeOut)
def update_employee(id: int, updated: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp.name = updated.name
    emp.location = updated.location
    db.commit()
    db.refresh(emp)
    return emp

@app.delete("/employees/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"detail": "Deleted"}
