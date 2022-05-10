import weakref

from django.conf import settings

from taiga.base.utils import json
from taiga.celery import app
from taiga.celery import celeryconfig
from taiga.celery import exceptions

from . import models


logger = logging.getLogger("taiga.celery")


def _get_task(task_name):
    """
    Get a task by name.

    Raises:
        exceptions.TaskNotFoundError: If a task with the specified name is not found.

    Returns:
        celery.Task: The task with the specified name.
    """
    try:
        return app.tasks.get(task_name)
    except KeyError:
        raise exceptions.TaskNotFoundError("Task not found: {}".format(task_name))


def _get_and_deserialize_args(task_name, json_args):
    """
    Deserialize the arguments of a task.

    Args:
        task_name (str): The name of the task.
        json_args (str): The arguments of the task
