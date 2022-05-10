import socket
import ssl
import struct
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import protocol
from . import sslextras
from .proxy import Proxy, ProxyError
from .sslproto import SSLProtocol


class ConnectionContext(object):
    """
    This class abstracts all socket operations and is used by the
    :class:`ConnectionHolder` to manage the underlying socket.

    :ivar ssl: If true, :meth:`_connect` will wrap the socket in an SSL socket
        using the :func:`ssl.wrap_socket` method.
    :ivar timeout: The socket timeout.
    :ivar source_address: The local address to use when connecting.
    """
    def __init__(self, ssl=False, timeout=None, source_address=None):
        self.ssl = ssl
        self.timeout = timeout
        self.source_address = source_address

    def _connect(self, host, port, socket_options):
        """
        Connect to the given host and port and
