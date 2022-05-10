import selectors
import sys
import time
import os

from . import exceptions
from . import utils
from . import socks5
from . import http_common


class HttpClient:
    "Python HTTP Client"

    def __init__(self, max_connections=10):
        self._max_connections = max_connections
        self._connections = set()
        self._selector = selectors.DefaultSelector()
        self._stopped = False
        self._stopped_event = threading.Event()

    def close(self):
        """
        Close all connections and stop the client.
        """
        self._stopped = True
        self._stopped_event.set()
        self._selector.close()
        for conn in self._connections:
            conn.close()
        self._connections.clear()

    def _close_connection(self, conn):
        """
        Remove a connection from the pool and close it.
        """
