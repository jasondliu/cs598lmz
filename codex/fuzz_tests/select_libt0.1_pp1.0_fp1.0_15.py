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


class Server(object):
    """
    A server that listens for connections from clients.

    :param str host: The host to listen on.
    :param int port: The port to listen on.
    :param str key: The key to use for encryption.
    :param bool debug: Whether to enable debug logging.
    """

    def __init__(self, host, port, key, debug=False):
        self._host = host
        self._port = port
        self._key = key
        self._debug = debug

        self._server_socket = None
        self._clients = {}
        self._client_lock = threading.Lock()
        self._running = False
        self._thread = None

    def start(self):
        """
       
