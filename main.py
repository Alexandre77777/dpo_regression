from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

with open('best_regression_model.pkl', 'rb') as f:
    saved_objects = pickle.load(f)

feature_engineering = saved_objects["pipeline"]
best_model = saved_objects["model"]

@app.post('/predict')
async def predict(input_data: InputData):
    X_new = np.array([[
        input_data.MedInc,
        input_data.HouseAge,
        input_data.AveRooms,
        input_data.AveBedrms,
        input_data.Population,
        input_data.AveOccup,
        input_data.Latitude,
        input_data.Longitude ]
        ]
 )
    X_new_transformed = feature_engineering.transform(X_new)

    prediction = best_model.predict(X_new_transformed)

    return {'prediction': float(prediction[0])}


