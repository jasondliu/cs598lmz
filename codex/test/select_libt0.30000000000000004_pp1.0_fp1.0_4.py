import select
import socket
import sys
import time

from . import __version__
from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_server_socket = None
_g_server_socket_port = None
_g_server_socket_thread = None
_g_server_socket_thread_running = False
_g_server_socket_thread_stop_event = threading.Event()
_g_server_socket_thread_stop_event.set()
_g_server_socket_thread_stop_event_lock = threading.Lock()

_g_server_socket_thread_stop_event_lock.acquire()
_g_server_socket_thread_stop_event.clear()
_g_server_socket_thread_stop_event_lock.release()


def _server_socket_thread_func():
    global _g_server_socket_thread_running
