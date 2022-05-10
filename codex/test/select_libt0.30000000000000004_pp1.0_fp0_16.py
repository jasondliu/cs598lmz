import select
import socket
import sys
import threading
import time

from . import common
from . import config
from . import log
from . import protocol
from . import util

_logger = log.get_logger(__name__)


class Server(object):
    """
    A server that accepts connections from clients and manages them.

    :param config: The server configuration.
    :type config: :class:`~.config.Config`
    :param client_class: The class to use for clients.
    :type client_class: :class:`~.client.Client`
    """

    def __init__(self, config, client_class=None):
        self._config = config
        self._client_class = client_class or Client
        self._clients = {}
        self._listener = None

    def start(self):
        """
        Start the server.
        """
        self._listener = Listener(self._config, self._client_class)
