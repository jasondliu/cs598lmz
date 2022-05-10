import select
import socket
import sys
import threading
import time
import traceback

from . import __version__
from . import _logging
from . import _util
from . import _x11

_logger = _logging.get_logger(__name__)


class _Connection(object):
    """
    A connection to a remote host.

    This class provides a file-like interface to the connection, and
    handles the details of setting up the connection and closing it
    when done.

    """

    def __init__(self, host, port, socket_factory=None):
        self._host = host
        self._port = port
        self._socket_factory = socket_factory
        self._socket = None
        self._file = None

    def __enter__(self):
        self._socket = self._socket_factory() if self._socket_factory else socket.socket()
        self._socket.connect((self._host, self._port))
        self._file = self._socket.makefile('rw')
        return self

