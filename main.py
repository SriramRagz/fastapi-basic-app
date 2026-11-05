from fastapi import FastAPI

app = FastAPI(title="My First FastAPI App")

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to FastAPI."}
