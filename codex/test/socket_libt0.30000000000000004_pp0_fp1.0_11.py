import socket
import sys
import time

from . import exceptions
from . import utils
from . import __version__

try:
    import ssl
except ImportError:
    ssl = None


class Connection(object):
    """
    A connection to a Redis server.

    This class abstracts the socket connection and the Redis protocol
    negotiation. It can be used as a context manager.
    """
