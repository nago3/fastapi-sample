"""This module contains the FastAPI application."""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Returns a dictionary with a greeting message.

    :return: A dictionary with the greeting message.
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Retrieve an item by its ID.

    Parameters:
        item_id (int): The ID of the item to retrieve.
        q (str, optional): A query parameter.
    Returns:
        dict: A dictionary containing the item ID and the query parameter, if provided.
    """
    return {"item_id": item_id, "q": q}
