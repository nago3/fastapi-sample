# FastAPI sample code repository

This is a sample code repository for FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Import Process

To use FastAPI, you need to install it first. You can do this by running the following command:

```sh
$ pip install "fastapi[all]"
```

You also need to install an ASGI server, for example, Uvicorn. You can install it with pip:

```sh
$ pip install uvicorn
```

## Run the server

To run the server, please execute the following from the root directory:

- This will call the `app` object from the `main` module and run it with Uvicorn.

```sh
$ uvicorn main:app --reload
```

Then, open your browser and go to http://localhost:8000/items/1.
You will see the response as below:

```json
{ "item_id": 1, "q": null }
```

and add a query parameter, for example, http://localhost:8000/items/1?q=somequery.

```json
{ "item_id": 1, "q": "somequery" }
```

## Run the tests

To run the tests, we use the `pytest` framework. To run the tests,

import the `pytest` package and run the following command:

```sh
$ pip install pytest
```

Then, please execute the following from the root directory:

```sh
$ pytest
```

## Deployment

This project is deployed on AWS Elastic Beanstalk. You can find the deployment URL in the description of this repository.

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- [Pytest](https://docs.pytest.org/en/stable/) - Testing framework
