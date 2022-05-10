import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import protocol
from . import utils

__all__ = ['Connection']


class Connection(object):
    """
    A connection to a Redis server.

    This class abstracts the socket connection and the Redis protocol. It
    provides methods to execute Redis commands.

    Any command raising an exception does so by calling ``raise`` and is
    therefore safe to be used in a ``with`` statement. The exceptions are
    never caught by the library.

    Example usage::

        >>> from redis import Connection
        >>> c = Connection(host='localhost', port=6379)
        >>> c.connect()
        >>> c.execute_command('PING')
        'PONG'
        >>> c.disconnect()

    This class can also be used as a context manager around a ``with``
    statement to automatically connect and disconnect::

        >>> with Connection(...) as c:
        ...     c.execute_command('PING')
        ...
        'PONG'
