import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version

_logger = log.get_logger(__name__)


class Client(object):
    """
    A client for the server.
    """

    def __init__(self, host, port, name, password,
                 reconnect_interval=config.DEFAULT_RECONNECT_INTERVAL):
        """
        Initialize the client.

        :param host: The host to connect to.
        :param port: The port to connect to.
        :param name: The name of the client.
        :param password: The password of the client.
        :param reconnect_interval: The interval in seconds between
            reconnection attempts.
        """
        self._host = host
        self._port = port
        self._name = name
        self._password = password
        self._reconnect_interval = reconnect_interval
        self._socket = None
        self._socket_lock = threading.Lock()
        self
