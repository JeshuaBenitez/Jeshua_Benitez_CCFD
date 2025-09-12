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
class InputData(BaseModel):
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
@app.post("/score", response_model=OutputData)
def score(data: InputData):
    # dict() es correcto con pydantic v1 (como en tu requirements)
    arr = np.array([v for _, v in data.dict().items()]).reshape(1, -1)
    prob = model.predict_proba(arr)[:, -1]
    # buena práctica: convertir a float nativo para JSON limpio
    return {"score": float(prob[0])}
