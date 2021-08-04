from os import getenv

from celery import Celery
from flask import Flask
from flask_cors import CORS

from config import app_config


def make_celery(app):
    """Initialize Celery"""
    celery = Celery(
        app.import_name,
        broker=app.config["CELERY_BROKER_URL"],
        backend=app.config["CELERY_RESULT_BACKEND"],
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


# create Flask app
app = Flask(__name__)
app.config.from_object(app_config[getenv("ENVIRONMENT")])
CORS(app)

# create Celery app
celery = make_celery(app)

# add routes to Flask app
with app.app_context():
    from app import routes
