# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:33:51 2024

@author: khaws
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    temperature:float
    humidity:int
    dew_point:float
    sea_level_pressure:float
    cloud:int
    wind_speed:float
    
    
prediction_model = pickle.load(open('cloudburst_prediction_trained.sav', 'rb'))


@app.post('/predict')
def cloudburst_pred(input_parameters: model_input):
    temp = input_parameters.temperature
    hum = input_parameters.humidity
    dew = input_parameters.dew_point
    pressure = input_parameters.sea_level_pressure
    cloud = input_parameters.cloud
    wind = input_parameters.wind_speed

    input_list = [[temp, hum, dew, pressure, cloud, wind]]
    prediction = prediction_model.predict(input_list)

    return prediction[0]
    
    
    
