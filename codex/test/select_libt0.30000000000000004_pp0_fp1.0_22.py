import select
import socket
import sys
import threading
import time

from . import protocol
from . import util

logger = logging.getLogger(__name__)


class Server(object):
    """
    A server that accepts connections from clients and handles their requests.
    """

    def __init__(self, host, port, handler):
        """
        Create a server.

        :param host: The hostname to bind to.
        :param port: The port to bind to.
        :param handler: The handler to use for incoming requests.
        """
        self._host = host
        self._port = port
        self._handler = handler
        self._server_socket = None
        self._connections = {}
        self._connections_lock = threading.Lock()
        self._stop_event = threading.Event()
        self._thread = None

