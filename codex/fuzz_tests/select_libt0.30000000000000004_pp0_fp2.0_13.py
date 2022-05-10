import select
import socket
import sys
import time

from . import constants
from . import exceptions
from . import utils


class Connection(object):
    """
    A connection to a remote host.

    :param host: The host to connect to.
    :type host: str
    :param port: The port to connect to.
    :type port: int
    """
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._socket = None
        self._connected = False
        self._timeout = None
        self._read_timeout = None
        self._write_timeout = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def connect(self):
        """
        Connect to the remote host.
        """
        if self._connected:
            raise exceptions.ConnectionError('Already connected')

        self._socket = socket.socket(socket.AF_INET, socket
