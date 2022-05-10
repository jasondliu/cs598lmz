import socket
import sys
import time

from . import config
from . import log
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_aio_client = None


class AioClient(object):
    def __init__(self):
        self._sock = None
        self._sock_file = None
        self._sock_file_lock = threading.Lock()
        self._sock_file_cond = threading.Condition(self._sock_file_lock)
        self._sock_file_cond_wait_time = 0.1
        self._sock_file_cond_wait_time_max = 5.0
        self._sock_file_cond_wait_time_step = 0.1
        self._sock_file_cond_wait_time_min = 0.1
        self._sock_file_cond_wait_time_reset_step = 0.1
        self._sock_file_cond_wait_time_
