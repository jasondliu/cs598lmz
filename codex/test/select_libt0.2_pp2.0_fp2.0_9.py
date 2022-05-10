import select
import socket
import sys
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version
from . import worker
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_worker_process = None
_g_worker_process_lock = threading.Lock()


def _get_worker_process():
    global _g_worker_process
    with _g_worker_process_lock:
        return _g_worker_process


def _set_worker_process(worker_process):
    global _g_worker_process
    with _g_worker_process_lock:
        _g_worker_process = worker_process


def _get_worker_process_lock():
    global _g_worker_process_lock
    return _g_worker_process_lock


def _get_worker_process_lock_with_log():
    global _g_worker_process_lock
