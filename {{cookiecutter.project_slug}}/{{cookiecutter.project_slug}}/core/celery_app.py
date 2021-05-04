from celery import Celery

celery_app = Celery("worker", broker="amqp://guest@queue//")

celery_app.conf.task_routes = {"{{cookiecutter.project_slug}}.worker.test_celery": "main-queue"}
