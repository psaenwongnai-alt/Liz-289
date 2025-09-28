# FastAPI/Flask backend ตัวอย่าง
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello from backend"}
