import weakref

from tornado import gen
from tornado.log import app_log

from .client import Client
from .constants import (
    DEFAULT_CONNECT_TIMEOUT, DEFAULT_READ_TIMEOUT, DEFAULT_WRITE_TIMEOUT)
from .connection import Connection
from .dispatcher import Dispatcher
from .errors import (
    ConnectionClosedError, ConnectionError, ConnectionTimeoutError)
from .event import Event
from .message import Message
from .options import Options
from .utils import configure_logging


class ConnectionPool(object):
    """Connection pool for asynchronous NATS clients.

    An asynchronous NATS client maintains a connection pool of TCP connections
    to a NATS server that are used for publishing and receiving messages.

    The client will create connections when it is created and will establish
    new connections when connections are lost.

    The connection pool is a :class:`~asyncio.Queue` of :class:`Connection`
    instances.
    """

    def __init__(self, *, loop, disconnect_cb=None, max_connections=1):
        self._loop
