import select
import socket
import sys
import threading
import time
import traceback

from . import __version__
from . import constants
from . import exceptions
from . import utils
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_thread_pool = []


class _ThreadPool(object):
    def __init__(self, max_thread_num):
        self._max_thread_num = max_thread_num
        self._thread_num = 0
        self._lock = threading.Lock()
        self._thread_pool = []

    def add_thread(self, thread):
        with self._lock:
            self._thread_pool.append(thread)
            self._thread_num += 1
