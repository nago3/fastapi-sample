# FastAPI sample

## Summary

We learned how to use FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints...

- Automatic generation of API documents using type hints, which is a feature
- Database operation using SQLAlchemy
- Database migration using alembic

## Run the server

```sh
$ python3 app.py
```

## Use DB with SQLAlchemy, Alembic

### Install

```sh
$ pip install alembic SQLAlchemy
```

### Create a new migration

```sh
$ alembic init migrations
```

### Create a new database

```sh
$ alembic revision --autogenerate -m "create todo table"
```

### Upgrade the database

```sh
$ alembic upgrade head
```

### API Test with FastAPI API Document

```sh
$ python3 app.py
```

Open your browser and go to `http://http://127.0.0.1:8000/docs`.
