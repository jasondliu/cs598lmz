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
from . import events
from . import log
from . import message
from . import protocol
from . import util

logger = log.get_logger(__name__)


class Connection(object):
    """
    A connection to a remote host.

    :param host: The host to connect to.
    :type host: str
    :param port: The port to connect to.
    :type port: int
    :param ssl: Whether to use SSL.
    :type ssl: bool
    :param timeout: The timeout for the connection.
    :type timeout: float
    :param loop: The event loop to use.
    :type loop: :class:`asyncio.BaseEventLoop`
    """

    def __init__(self, host, port, ssl=False, timeout=None, loop=None):
        self.host = host
        self.port = port
        self.ssl = s
