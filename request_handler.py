from fastapi import FastAPI, HTTPException
import patient_service
from models import PatientModel
app = FastAPI()


@app.get("/patient/{patient_id}")
def patient_details(patient_id: str):
    result = patient_service.get_patient(patient_id)
    return result


@app.post("/patient")
def add_patient(patient: PatientModel):
    result = patient_service.add_patient(patient)
    if not result:
        raise HTTPException(status_code=400, detail="Patient already exists!")
    else:
        return result