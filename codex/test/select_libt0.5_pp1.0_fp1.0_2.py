import select
import socket
import sys
import time
import traceback
import threading

from . import protocol
from . import util
from . import exceptions
from . import __version__

__all__ = ["Connection", "connect", "open", "DEFAULT_PORT", "DEFAULT_HOST"]

DEFAULT_PORT = 8000
DEFAULT_HOST = "localhost"

class Connection(object):
    """
    A connection to a remote livereload server.

    You can use :func:`connect` to create a connection::

        connection = livereload.Connection(('localhost', 35729))

    .. seealso:: :func:`connect`
    """

    def __init__(self, hostport):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(hostport)
        self.socket.setblocking(0)
        self.buffer = b""
