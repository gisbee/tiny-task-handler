import subprocess
from http import HTTPStatus
from os.path import isfile, join

from flask import jsonify, request

from app import app, celery
from app.utils import create_task_commands


@celery.task(bind=True)
def task_handler(self, params):
    """
    Execute a task in background using Celery
    Note: Task name and ID can be fetched with
          self.request.shadow and self.request.id respectively
    """
    commands = create_task_commands(params)
    for command in commands:
        subprocess.check_call(command, shell=True)


@app.route("/task/<name>", methods=["POST"])
def endpoint(name):
    """Default route to run a task"""

    config_file = join(
        app.config["BASEDIR"],
        "app",
        "configs",
        f"{name}.json",
    )

    if not isfile(config_file):
        return (
            jsonify({"message": f"Unknown task: {name}"}),
            HTTPStatus.NOT_FOUND,
        )

    params = request.get_json(force=True)
    params["config_file"] = config_file

    task = task_handler.apply_async(shadow=name, args=[params])

    return task.id, HTTPStatus.OK
