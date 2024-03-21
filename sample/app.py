""""This module contains the FastAPI application."""

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint of the FastAPI application.

    Returns:
        dict: A dictionary with a single key-value pair representing the message.
    """
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
