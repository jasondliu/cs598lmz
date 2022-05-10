import select
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

_logger.info('{} {}'.format(__name__, __version__))


class _Socket(object):
    def __init__(self, sock):
        self._sock = sock
        self._sock.setblocking(False)
        self._recv_buffer = b''
        self._send_buffer = b''

    def fileno(self):
        return self._sock.fileno()

    def send(self, data):
        self._send_buffer += data

    def recv(self, size):
        if len(self._recv_buffer) < size:
            return None
        data = self._recv_buffer[:size]
        self._recv_buffer = self._recv_buffer[size:]
        return data

    def close(self):
       
