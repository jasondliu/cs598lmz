import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import constants
from . import log
from . import messages
from . import util
from . import version

def _get_socket_path():
    return os.path.join(config.get_config_dir(), 'socket')

def _get_socket_path_old():
    return os.path.join(config.get_config_dir(), 'socket.old')

def _get_socket_path_tmp():
    return os.path.join(config.get_config_dir(), 'socket.tmp')

class _Server(threading.Thread):
    def __init__(self, socket_path, socket_path_old, socket_path_tmp,
                 on_message_received):
        super().__init__()
        self._socket_path = socket_path
        self._socket_path_old = socket_path_old
        self._socket_path_tmp = socket_path_tmp
        self._on_message_received = on_message_received
