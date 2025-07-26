from fastapi import FastAPI, UploadFile, File
from app.processor import extract_tags

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()

    with open("temp.wav", "wb") as f:
        f.write(contents)

    tags = extract_tags("temp.wav")
    return tags
