import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import util

_logger = log.get_logger(__name__)


class _Connection(object):
    """
    A connection to a remote host.

    This class is not thread-safe.
    """

    def __init__(self, host, port, timeout):
        self._host = host
        self._port = port
        self._timeout = timeout
        self._socket = None

    def __enter__(self):
        self._socket = socket.create_connection((self._host, self._port), self._timeout)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._socket.close()

    def send(self, data):
        """
        Send data to the remote host.

        :param data: The data to send.
        :type data: bytes
        """
        self._socket.sendall(data
