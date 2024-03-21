"""Define the types of data that can be received by the API."""
from pydantic import BaseModel


class PostTodo(BaseModel):
    """Define the title of a Todo item."""
    title: str
