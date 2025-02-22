from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import modeltrain

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str


@app.post("/check_spam", response_class=JSONResponse)
async def check_spam(input: TextInput):
    soup = BeautifulSoup(input.text, "html.parser")
    clean_text = soup.get_text(separator=" ")
    predictionResult = modeltrain.PredictScamEmail(clean_text)
    print(predictionResult)
    return {"is_spam": predictionResult}
