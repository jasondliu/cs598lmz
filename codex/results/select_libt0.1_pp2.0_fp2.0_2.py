import select
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
from . import messages
from . import protocol
from . import util

_logger = log.get_logger(__name__)


class Client(object):
    """
    A client for the server.

    This class is thread-safe.
    """

    def __init__(self, host, port, timeout=None):
        """
        Initializes a new instance of the Client class.

        :param host: The hostname or IP address of the server.
        :param port: The port of the server.
        :param timeout: The timeout in seconds for socket operations.
        """
        self._host = host
        self._port = port
        self._timeout = timeout
        self._socket = None
        self._lock = threading.RLock()
        self._connected = False
        self._connect_time = None
        self._disconnect_time = None
        self._last_activity
