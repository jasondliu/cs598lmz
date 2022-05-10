import select
import socket
import sys
import threading
import time

from . import constants
from . import exceptions
from . import util

logger = logging.getLogger(__name__)


class Connection(object):
    """
    A connection to a remote host.

    :param host: The host to connect to.
    :type host: str
    :param port: The port to connect to.
    :type port: int
    :param timeout: The timeout for the connection.
    :type timeout: float
    :param ssl: Whether to use SSL.
    :type ssl: bool
    :param ssl_options: SSL options.
    :type ssl_options: dict
    :param keepalive: Whether to keep the connection alive.
    :type keepalive: bool
    :param keepalive_idle: The idle time before sending a keepalive packet.
    :type keepalive_idle: int
    :param keepalive_interval: The interval between keepalive packets.
    :type keepalive_interval: int
    :param
