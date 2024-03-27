from typing import Union

from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/talk")
async def post_audio():
    audio_file = open("/audio")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return {"Hello": "World"}