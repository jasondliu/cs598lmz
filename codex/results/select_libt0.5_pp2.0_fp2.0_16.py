import select
import socket
import threading
import time

from . import exceptions
from . import utils

_logger = logging.getLogger(__name__)


class Server:
    """
    A server that listens for incoming connections and handles them in a separate thread.
    """
    def __init__(self, host, port, handler_factory, timeout=None, backlog=10,
                 reuse_address=True, reuse_port=False, allow_reuse_address=True):
        """
        :param host: The IP address to listen on.
        :param port: The port to listen on.
        :param handler_factory: A callable that returns a :class:`~.Handler` instance.
        :param timeout: The timeout in seconds for the socket.
        :param backlog: The backlog for the server socket.
        :param reuse_address: Whether to set the ``SO_REUSEADDR`` socket option.
        :param reuse_port: Whether to set the ``SO_REUSEPORT`` socket option.
        :param allow_reuse_address: Whether to set
