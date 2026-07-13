#main
#created by: Brandon Donaldson
import uvicorn
#libraries
from fastapi import FastAPI
from src.simulation import run_simulation

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ping": "pong"}

@app.get("/simulate")
def simulate(mass: float, damping: float, stiffness: float, x0: float, v0: float, duration: float):
    return run_simulation(mass, damping, stiffness, x0, v0, duration)
    return result