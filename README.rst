Cookiecutter FastAPI
====================

Cookiecutter_ template for a FastAPI app.


Features
--------
- contains no models aside from basic user model
- supports typical authentication protocols
- poetry support
- tox support
- tested on Python 3.8

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter


Quickstart
----------

Install Cookiecutter::

    pip install -U cookiecutter

Generate a project::

    cookiecutter https://github.com/chungg/cookiecutter-fastapi.git

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
