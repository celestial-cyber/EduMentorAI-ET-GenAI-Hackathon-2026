from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "EduMentor AI Backend Running"}
