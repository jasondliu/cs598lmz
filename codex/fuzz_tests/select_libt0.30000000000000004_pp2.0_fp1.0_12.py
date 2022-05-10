import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import exceptions
from . import log
from . import util

_logger = log.get_logger(__name__)


class _SockWrapper:
    """
    Wrapper for a socket that provides a file-like interface.
    """
    def __init__(self, sock):
        self._sock = sock
        self._sock.setblocking(False)
        self._buf = b''

    def read(self, n):
        """
        Read up to n bytes from the socket.
        """
        while len(self._buf) < n:
            try:
                self._buf += self._sock.recv(config.BUFFER_SIZE)
            except socket.error:
                break
        ret = self._buf[:n]
        self._buf = self._buf[n:]
        return ret

    def write(self, data):
        """
        Write data to the socket.
        """
        self._sock.send
