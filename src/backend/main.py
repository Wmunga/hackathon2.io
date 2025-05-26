from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from . import database
from .database import Patient, Appointment

# Create database tables
database.create_tables()

app = FastAPI(title="HealthTech Reminder System")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Patient routes
@app.get("/patients/", response_model=List[dict])
async def get_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "email": p.email,
            "phone": p.phone,
            "created_at": p.created_at
        }
        for p in patients
    ]

@app.post("/patients/", response_model=dict)
async def create_patient(
    name: str,
    email: str,
    phone: str,
    db: Session = Depends(get_db)
):
    # Check if patient with email already exists
    if db.query(Patient).filter(Patient.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new patient
    patient = Patient(name=name, email=email, phone=phone)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    
    return {
        "id": patient.id,
        "name": patient.name,
        "email": patient.email,
        "phone": patient.phone,
        "created_at": patient.created_at
    }

# Appointment routes
@app.get("/appointments/", response_model=List[dict])
async def get_appointments(db: Session = Depends(get_db)):
    appointments = db.query(Appointment).all()
    return [
        {
            "id": a.id,
            "patient_id": a.patient_id,
            "patient_name": a.patient.name,
            "datetime": a.datetime,
            "type": a.type,
            "notes": a.notes,
            "status": a.status,
            "created_at": a.created_at
        }
        for a in appointments
    ]

@app.post("/appointments/", response_model=dict)
async def create_appointment(
    patient_id: int,
    datetime_str: str,
    type: str,
    notes: str = None,
    db: Session = Depends(get_db)
):
    # Check if patient exists
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Parse datetime string
    try:
        appointment_datetime = datetime.fromisoformat(datetime_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format")
    
    # Create new appointment
    appointment = Appointment(
        patient_id=patient_id,
        datetime=appointment_datetime,
        type=type,
        notes=notes
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    
    return {
        "id": appointment.id,
        "patient_id": appointment.patient_id,
        "patient_name": patient.name,
        "datetime": appointment.datetime,
        "type": appointment.type,
        "notes": appointment.notes,
        "status": appointment.status,
        "created_at": appointment.created_at
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 