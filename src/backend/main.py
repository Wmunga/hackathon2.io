from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="HealthTech Reminder System")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic models
class Patient(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    phone: str
    created_at: datetime = datetime.now()

class Appointment(BaseModel):
    id: Optional[int] = None
    patient_id: int
    datetime: datetime
    type: str
    notes: Optional[str] = None
    status: str = "scheduled"

# Basic routes
@app.get("/")
async def root():
    return {"message": "Welcome to HealthTech Reminder System API"}

@app.get("/patients/", response_model=List[Patient])
async def get_patients():
    # TODO: Implement database connection
    return []

@app.post("/patients/", response_model=Patient)
async def create_patient(patient: Patient):
    # TODO: Implement database connection
    return patient

@app.get("/appointments/", response_model=List[Appointment])
async def get_appointments():
    # TODO: Implement database connection
    return []

@app.post("/appointments/", response_model=Appointment)
async def create_appointment(appointment: Appointment):
    # TODO: Implement database connection
    return appointment

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 