import socket
import sys
import time

from . import config
from . import utils

log = utils.get_logger(__name__)


def _get_socket_path():
    return os.path.join(config.get_config_dir(), 'sock')


def _get_socket():
    return socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


def _connect_socket():
    sock_path = _get_socket_path()
    sock = _get_socket()
    try:
        sock.connect(sock_path)
    except socket.error as e:
        if e.errno == errno.ECONNREFUSED:
            raise utils.NoDaemonError(
                'No daemon running at {}'.format(sock_path))
        else:
            raise
    return sock


def _send_command(command):
    sock = _connect_socket()
    try:
        sock.sendall(command)
        sock.shutdown(socket.SHUT_WR)
        response =
