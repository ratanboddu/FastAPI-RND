from fastapi import FastAPI
import uvicorn
import logging
import requests

app = FastAPI()
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/data")
def get_data():
    logger.debug("Inside get_data()")
    return "Data"


@app.get("/items/{item_id}")
def fetch_data(item_id: int, q: str = None):
    # Checking if requests works in FastAPI
    data = requests.get("http://0.0.0.0:8000/data")
    logger.debug("Done fetching data")
    return {"item_id": item_id, "q": q, "data": data.json()}


if __name__ == '__main__':
    uvicorn.run(app=app)
