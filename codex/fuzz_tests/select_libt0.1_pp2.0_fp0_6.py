import select
import socket
import sys
import threading
import time
import traceback

from . import __version__
from . import config
from . import constants
from . import errors
from . import log
from . import utils
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_thread_pool = []
_g_thread_pool_lock = threading.Lock()


def _thread_pool_append(thread):
    with _g_thread_pool_lock:
        _g_thread_pool.append(thread)


def _thread_pool_remove(thread):
    with _g_thread_pool_lock:
        _g_thread_pool.remove(thread)


def _thread_pool_join_all():
    with _g_thread_pool_lock:
        for thread in _g_thread_pool:
            thread.join()


class _Thread(threading.Thread):
    def __init__(self, name, target, args=None, kwargs=None):
        super(_
