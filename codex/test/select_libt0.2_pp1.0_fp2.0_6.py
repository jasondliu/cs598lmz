import select
import socket
import sys
import time

from . import config
from . import log
from . import util

logger = log.get_logger()

def _get_sock(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    return sock

def _get_client_sock(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock

def _get_socks(host, port):
    sock = _get_sock(host, port)
    client_sock = _get_client_sock(host, port)
    return sock, client_sock

def _get_socks_with_timeout(host, port, timeout):
    sock = _
