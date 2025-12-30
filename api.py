import joblib
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.staticfiles import StaticFiles



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
# Enable CORS so your frontend can send data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Titanic(BaseModel):
    Pclass:int
    Sex:str
    Age:int
    Siblings:int
    Parents:int
    ticket_price:int
    place:str

@app.get("/", response_class=HTMLResponse)
def home():
    return open("index.html").read()

@app.post('/predict')
def predict_outcome(d: Titanic):
    pipe = joblib.load('TitanicPipeline.pkl')

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
    return {"survived": int(result)}
