from typing import Optional

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
import scraper

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get-news", response_class=UJSONResponse)
def read_root():
    return scraper.data_list


@app.get("/get-newse")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
