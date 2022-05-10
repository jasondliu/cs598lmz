import socket
import sys
import time
import traceback

from . import __version__
from . import constants
from . import exceptions
from . import utils
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_client_socket = None
_g_client_socket_lock = threading.Lock()


def _connect_to_server(host, port):
    global _g_client_socket
    _g_client_socket_lock.acquire()
    try:
        if _g_client_socket is not None:
            return _g_client_socket
        _logger.info('connect to server {}:{}'.format(host, port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        _g_client_socket = sock
        return _g_client_socket
    finally:
        _g_client_socket_lock.release()


def _close_client_socket():
    global _g_client_
