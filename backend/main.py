from fastapi import FastAPI
from pydantic  import BaseModel
import joblib

model = joblib.load("spam_model.pkl")

app = FastAPI(title="Spam Detection API",description="predicts whether the message is spam or not", version="1.0")
class Messageinput(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status":"Spam Detection API is Running"}

@app.post("/predict")
def predict(data:Messageinput):
    prediction = model.predict([data.message])[0]

    if prediction == 1:
        result ="Spam"
    else:
        result = "Not Spam"

    return{
    "prediction":int(prediction),"result":result
    }