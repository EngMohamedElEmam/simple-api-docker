import time

from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/version")
def get_version() -> str:
    time.sleep(15)
    return "v0.1"
