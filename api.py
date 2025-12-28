
import joblib
from pydantic import BaseModel,Field
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

class titanic(BaseModel):
    Pclass:int
    Sex :str
    Age:int
    Siblings:int
    Parents:int
    ticket_price:int
    place:str

@app.post('/predict')
def presict_outcome(d:titanic):
    pipe=joblib.load('TitanicPipeline.pkl')

    data = pd.DataFrame([{
    'Pclass': d.Pclass,
    'Sex': d.Sex,
    'Age': d.Age,
    'Siblings': d.Siblings,    
    'Parents': d.Parents,
    'Fare': d.ticket_price,
    'Embarked': d.place
    }])




    result = pipe.predict(data)[0]
    return JSONResponse(status_code=200,content={'message':result})



