import socket
import sys
import threading
import time

from . import constants
from . import exceptions
from . import utils
from .constants import (
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_TIMEOUT,
    DEFAULT_TTL,
    DEFAULT_USER_AGENT,
    DEFAULT_VERBOSITY,
)
from .exceptions import (
    ConnectionError,
    ProtocolError,
    ResponseError,
    TimeoutError,
)
from .protocol import (
    Connection,
    Response,
)
from .utils import (
    get_logger,
    is_iterable,
    is_string,
    is_tuple,
)


class Client(object):
    """
    Client for the StatsD server.

    :param host: Hostname or IP address of the StatsD server.
    :type host: str
    :param port: Port of the StatsD server.
    :type port: int
    :param prefix: Prefix to prepend to all metrics.
    :type prefix: str

