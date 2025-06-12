# src/api/api.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("models/svr_model.pkl")

# Select only the features used during model training
selected_features = [
    'setting_1', 'setting_2', 'setting_3',
    's_2', 's_3', 's_4', 's_7', 's_8',
    's_9', 's_11', 's_12', 's_13', 's_15', 's_17'
]

class InputData(BaseModel):
    setting_1: float
    setting_2: float
    setting_3: float
    s_2: float
    s_3: float
    s_4: float
    s_7: float
    s_8: float
    s_9: float
    s_11: float
    s_12: float
    s_13: float
    s_15: float
    s_17: float

class BatchInput(BaseModel):
    data: list[InputData]

@app.post("/predict")
def predict(input_data: InputData):
    df = pd.DataFrame([input_data.dict()])[selected_features]
    prediction = model.predict(df)[0]
    return {"predicted_rul": float(prediction)}

@app.post("/batch_predict")
def batch_predict(batch: BatchInput):
    df = pd.DataFrame([d.dict() for d in batch.data])[selected_features]
    predictions = model.predict(df).tolist()
    return {"predictions": predictions}

@app.get("/health")
def health_check():
    return {"status": "API is running", "model_loaded": model is not None}
