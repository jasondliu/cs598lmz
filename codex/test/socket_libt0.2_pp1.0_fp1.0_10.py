import socket
import sys
import threading
import time
import traceback

from . import config
from . import exceptions
from . import log
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_aio_server = None
_g_aio_server_lock = threading.Lock()
_g_aio_server_thread = None
_g_aio_server_thread_lock = threading.Lock()
_g_aio_server_thread_stop_event = threading.Event()
_g_aio_server_thread_stop_event.set()
_g_aio_server_thread_stop_event_lock = threading.Lock()


class AioServer(object):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._server = None
        self._server_thread = None
        self._server_thread_stop_event = None
        self._server_thread_
