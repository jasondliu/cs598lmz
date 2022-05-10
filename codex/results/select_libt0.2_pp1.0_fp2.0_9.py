import select
import socket
import sys
import threading
import time
import traceback

from . import base
from . import util
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_client_id = 0
_g_client_id_lock = threading.Lock()


class _Client(object):
    def __init__(self, client_id, client_socket, client_address):
        self.client_id = client_id
        self.client_socket = client_socket
        self.client_address = client_address
        self.client_socket.setblocking(False)
        self.client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.client_socket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 60)
        self.client
