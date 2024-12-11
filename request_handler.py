from fastapi import FastAPI, HTTPException
import patient_service

app = FastAPI()


@app.get("/patient/{patient_id}")
def patient_details(patient_id: str):
    result = patient_service.get_patient(patient_id)
    return result
