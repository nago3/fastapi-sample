""""This module contains the FastAPI application."""
import uvicorn
from fastapi import Depends, FastAPI
from models import TodoModel
from schemas import PostTodo
from settings import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    """Get a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    """Root endpoint of the FastAPI application.

    Returns:
        dict: A dictionary with a single key-value pair representing the message.
    """
    return {"Hello": "World"}


# データベースからToDo一覧を取得するAPI
@app.get("/todo")
def get_todo(db: Session = Depends(get_db)):
    """Specify the model defined in models.py in the query function
        and retrieve all records in the .all() function
    """
    return db.query(TodoModel).all()

# ToDoを作成するAPI
@app.post("/todo")
def post_todo(todo: PostTodo, db: Session = Depends(get_db)):
    """1. Create: create a model instance with the data received from the API.
        2. Register: insert the created model into the database.
        3. Commit: commit the changes to the database.
    """
    db_model = TodoModel(title = todo.title)  # 1.Create
    db.add(db_model)  # 2.Register
    db.commit()  # 3.Commit
    return {"message": "success"}

# ToDoを削除するAPI
@app.delete("/todo/{id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """1. Retrieve: retrieve the record to be deleted from the database.
        2. Delete: delete the retrieved record.
        3. Commit: commit the changes to the database.
    """
    target_todo = db.query(TodoModel).filter(TodoModel.id==todo_id).one()  # 1.Retrieve
    db.delete(target_todo)  # 2.Delete
    db.commit()  # 3.Commit
    return {"delete": "success"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
