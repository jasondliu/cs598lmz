import select
import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import version

log = log.get_logger()


def _get_socket_path():
    return os.path.join(config.get_config_dir(), 'control.sock')


def _get_socket_path_old():
    return os.path.join(config.get_config_dir(), 'control.sock.old')


def _get_socket_path_tmp():
    return os.path.join(config.get_config_dir(), 'control.sock.tmp')


class ControlSocket:
    def __init__(self, socket_path):
        self.socket_path = socket_path
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_UNIX)
        self.socket.setblocking(False)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

