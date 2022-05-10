import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import constants
from . import exceptions
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_sock_lock = threading.Lock()
_g_sock_list = []


def _close_all_sock():
    global _g_sock_list
    with _g_sock_lock:
        for sock in _g_sock_list:
            try:
                sock.close()
            except Exception as e:
                _logger.warning('_close_all_sock failed : {}'.format(e))
        _g_sock_list = []


def _add_sock(sock):
    global _g_sock_list
    with _g_sock_lock:
        _g_sock_list.append(sock)


def _remove_sock(sock):
    global _g_
