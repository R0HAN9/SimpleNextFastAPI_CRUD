from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    location: str

class EmployeeOut(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True
