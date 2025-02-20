from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class TextInput(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("FOSS.html", {"request": request})

@app.post("/check_spam", response_class=JSONResponse)
async def check_spam(input: TextInput):
    spam_words = ["win", "free", "offer", "click here"]
    is_spam = any(word in input.text.lower() for word in spam_words)
    return {"is_spam": is_spam}



