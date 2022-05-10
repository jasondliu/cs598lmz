import select
import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util


class Connection(object):
    """
    Represents a connection to a remote host.
    """

    def __init__(self, host, port, timeout=config.CONNECTION_TIMEOUT):
        self.host = host
        self.port = port
        self.timeout = timeout

        self.socket = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def connect(self):
        """
        Connects to the remote host.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)
        self.socket.connect((self.host, self.port))

    def close(self):
        """
        Closes the connection to the remote host.
        """
