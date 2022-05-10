import select
import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import version

__all__ = [
    'Client',
    'Server',
    'ServerConnection',
    'Connection',
]


class Connection(object):
    """
    A connection to a remote host.

    :param host: The host to connect to.
    :param port: The port to connect to.
    :param timeout: The timeout in seconds for the connection.
    """

    def __init__(self, host, port, timeout=30):
        self.host = host
        self.port = port
        self.timeout = timeout

        self.socket = None

    def __repr__(self):
        return '<%s %s:%s>' % (self.__class__.__name__, self.host, self.port)

    def connect(self):
        """
        Connect to the remote host.
        """

        self.socket = socket.socket(socket.AF_INET, socket.SOCK
