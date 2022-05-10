import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import log
from . import util
from . import version

_logger = log.get_logger(__name__)


class Server(object):
    """
    A server that listens for connections from clients.
    """

    def __init__(self, config_file):
        self._config = config.load_config(config_file)
        self._server_socket = None
        self._client_sockets = {}
        self._client_threads = {}
        self._client_thread_lock = threading.Lock()
        self._stop_event = threading.Event()

    def start(self):
        """
        Start the server.
        """
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server_socket
