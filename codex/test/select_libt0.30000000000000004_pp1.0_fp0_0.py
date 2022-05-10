import select
import socket
import sys
import time

from . import config
from . import log
from . import util
from . import xdg

LOG = log.get_logger(__name__)


def _get_socket_path():
    return os.path.join(xdg.get_runtime_dir(), 'sway.socket')


def _get_socket():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.setblocking(False)
    return sock


def _connect_socket(sock):
    sock.connect(_get_socket_path())


def _send_command(sock, command):
    sock.sendall(command.encode('utf-8'))


