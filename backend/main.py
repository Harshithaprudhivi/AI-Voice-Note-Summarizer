# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "AI Voice Note Summarizer is running"}


# from fastapi import FastAPI, UploadFile, File 
# import os, shutil
# from backend.services.transcriber import transcribe_audio

# app=FastAPI()

# UPLOAD_DIR = "backend/uploads"
# os.makedirs(UPLOAD_DIR, exist_ok= True)

# @app.get("/")
# def read_root():
#     return{"message": "AI Voice Note Summarizer is running"}

# @app.post("/upload-audio/")
# async def upload_audio(file:UploadFile = File(...)):
#     file_path = os.path.join(UPLOAD_DIR,file.filename)
    
#     with open(file_path,"wb") as buffer:
#         shutil.copyfileobj(file.file,buffer)
        
#     text = transcribe_audio(file_path)
    
#     return {
#         "filename" : file.filename,
#         "transcription" : text
#     }
    

# from backend.services.summarizer import summarize_text
# @app.post("/upload-audio/")
# async def upload_audio(file:UploadFile = File(...)):
#     file_path = os.path.join(UPLOAD_DIR,file.filename)
    
#     with open(file_path,"wb") as buffer:
#         shutil.copyfileobj(file.file,buffer)
        
#     text = transcribe_audio(file_path)
    
#     summary = summarize_text(text)

#     return {
#         "filename" : file.filename,
#         "transcription" : text,
#         "summary" : summary
#     }

from backend.services.summarizer import summarize_text
from fastapi import FastAPI, UploadFile, File
import os
import shutil

from backend.services.transcriber import transcribe_audio
from backend.services.summarizer import summarize_text

# ✅ app MUST be defined before using @app
app = FastAPI()

UPLOAD_DIR = "backend/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def read_root():
    return {"message": "AI Voice Note Summarizer is running"}


@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = transcribe_audio(file_path)
    summary = summarize_text(text)

    return {
        "filename": file.filename,
        "transcription": text,
        "summary": summary
    }
