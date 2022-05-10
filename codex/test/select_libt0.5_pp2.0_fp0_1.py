import select
import socket
from threading import Thread

from mrq.context import (
    connections,
    get_current_config,
    get_current_job,
    get_current_worker,
    get_current_task,
    get_current_greenlet,
    log,
    set_current_config,
    set_current_job,
    set_current_worker,
    set_current_task,
    set_current_greenlet
)
from mrq.job import Job
from mrq.logger import setup_logging
from mrq.queue import Queue
from mrq.task import Task
from mrq.utils import get_redis_connection, get_mongodb_connection, import_attribute, get_config_path
from mrq.worker import Worker


class WorkerAction(object):

    """ An action that can be performed by a worker. """

    def __init__(self, params):
        self.params = params
        self.worker = None
        self.queue = None
