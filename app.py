from fastapi import FastAPI
import uvicorn
from api import tareas

app = FastAPI(title="Mi primer CRUD con FastAPI")

app.include_router(tareas.router)

@app.get("/")
async def main():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)