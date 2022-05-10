import weakref
from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from . import utils
from .utils import *
from . import input_file
from . import output_file
from . import tasks
from . import exceptions

from .logger import get_logger

from . import resources_rc # NOQA

logger = get_logger(__name__)

def get_guts(name, force_check=False):
    """Tries to load a task by name"""
    if name in tasks.tasks_meta:
        return tasks.tasks_meta[name]
    if force_check:
        raise exceptions.TaskNotFound(name)
    tasks.scan()
    if name not in tasks.tasks_meta:
        raise exceptions.TaskNotFound(name)
    return tasks.tasks_meta[name]

def get_task(name, *args, **kwargs):
    """Tries to
