import select
import socket
import sys
import threading
import time
import traceback

from . import _util

_log = _util.get_logger(__name__)


class Server:
    """
    A server that listens for connections from clients.

    This class is not thread-safe.
    """

    def __init__(self, port, host='127.0.0.1'):
        """
        Create a new server that listens on the given port.
        """
        self._port = port
        self._host = host
        self._socket = None
        self._clients = []
        self._client_lock = threading.Lock()
        self._running = False
        self._thread = None
        self._on_connect = None
        self._on_disconnect = None
        self._on_message = None

    def start(self):
        """
        Start the server.

        This will start a new thread for the server.
        """
        if self._running:
            raise RuntimeError('server is already running')

