# FastAPI sample

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
