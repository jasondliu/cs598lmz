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
from . import utils

_logger = log.get_logger(__name__)


class Server(object):
    """
    A server that listens for connections from clients.

    :param config: The server configuration.
    :type config: :class:`~.config.ServerConfig`
    :param handler: The handler for incoming messages.
    :type handler: :class:`~.handler.Handler`
    """

    def __init__(self, config, handler):
        self._config = config
        self._handler = handler

        self._server_socket = None
        self._server_thread = None
        self._server_thread_lock = threading.Lock()
        self._server_thread_running = False

        self._client_sockets = {}
        self._client_threads = {}
        self._client_thread_locks = {}
        self
