import random
import string

from sqlalchemy.orm import Session
import typer

from {{cookiecutter.project_slug}} import crud, schemas
from {{cookiecutter.project_slug}}.db.session import SessionLocal

# make sure all SQL Alchemy models are imported (proj.db.base)
# before initializing DB otherwise, SQL Alchemy might fail to initialize relationships
# properly.
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

app = typer.Typer()


def gen_pass():
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(15))


@app.command(help='add a user to the app')
def create_user(username: str, password: str = None, is_superuser: bool = False):
    db = SessionLocal()
    user = crud.user.get_by_email(db, email=username)
    if not user:
        pw = password or gen_pass()
        user_in = schemas.UserCreate(
            email=username,
            password=pw,
            is_superuser=is_superuser
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
        typer.echo(f'Created user with password: {pw}')
    else:
        typer.echo('User already exists')


if __name__ == "__main__":
    app()
