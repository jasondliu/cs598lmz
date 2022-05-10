import socket
import sys
import time

from . import common
from . import config
from . import constants
from . import errors
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_aio_client = None
_g_aio_client_lock = threading.Lock()


class AioClient(object):
    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        self._timeout = timeout
        self._reader = None
        self._writer = None
        self._lock = threading.Lock()
        self._connect_lock = threading.Lock()
        self._connect_event = threading.Event()
        self._connect_event.set()
        self._connect_thread = None

    def _connect(self):
        self._connect_event.clear()
        self._connect_thread = threading.Thread(target=self._connect_thread_func)
        self._connect_thread
