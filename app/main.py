from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"get": "subscriptions"}


@app.get("/subscriptions/{subscription_id}")
def read_item(subscription_id: int, service: Union[str, None] = None):
    return {"subscription_id": subscription_id, "123": service}
