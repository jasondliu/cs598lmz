import selectors
import sys
import types

from . import config
from . import exceptions
from . import utils

log = logging.getLogger(__name__)


class _Selector(object):
    """
    Selector is a wrapper around selectors.DefaultSelector

    It exposes a simple interface for registering and unregistering
    sockets for reading and writing.
    """
    def __init__(self):
        self._selector = selectors.DefaultSelector()

    def register(self, sock, events, data=None):
        """
        Register a socket for events.

        :param sock: The socket to register.
        :param events: The events to register the socket for.
        :param data: The data to associate with the socket.
        """
        self._selector.register(sock, events, data)

    def unregister(self, sock):
        """
        Unregister a socket.

        :param sock: The socket to unregister.
        """
        self._selector.unregister(sock)

    def select(self, timeout):
        """
