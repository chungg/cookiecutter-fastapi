README
======

Application based on FastAPI


Quickstart
----------

Install Poetry and create virtualenv::

    pip install poetry
    cd <path to project>
    poetry shell

Create a `.venv` file::

    SERVER_NAME=<project_name>
    SERVER_HOST=<http://something>
    DATABASE_URI=postgresql://postgres:<pw>@localhost/test  # path to db

Run tests::

    tox


Start server::

    uvicorn {{cookiecutter.project_slug}}.main:app --host 0.0.0.0 --port 8080
