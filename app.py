from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware

# --- CORS ---
origins = ["*"]  # para pruebas locales; en prod usa dominios específicos

app = FastAPI(title="Credit card fraud")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,   # <— OJO: en plural
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Carga de modelo ---
model = load(pathlib.Path("model/creditcard-v1.joblib"))

# --- Esquemas ---
# ajuste class InputData, ya que el dataset tiene 30 datos.
class CreditCardFeatures(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

class OutputData(BaseModel):
    score: float = 0.80318881046519

# --- Endpoint de salud para probar rápido ---
@app.get("/")
def health():
    return {"status": "ok"}

# --- Endpoint de scoring ---
@app.post("/score")
def score(item: CreditCardFeatures):
    data = [list(item.dict().values())]
    proba = model.predict_proba(data)[0]   # Probabilidades
    prediction = int(model.predict(data)[0])  # Clase 0/1
    
    return {
        "prediction": prediction,
        "probability": {
            "no_fraud": float(proba[0]),
            "fraud": float(proba[1])
        }
    }

