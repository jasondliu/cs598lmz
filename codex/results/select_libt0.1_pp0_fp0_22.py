import select
import socket
import sys
import threading
import time

from . import constants
from . import exceptions
from . import utils
from . import version

__all__ = ['Connection']

LOGGER = logging.getLogger(__name__)


class Connection(object):
    """
    A connection to a RabbitMQ node.

    :param host: The hostname or IP address of the node.
    :type host: str
    :param port: The port number of the node.
    :type port: int
    :param user: The username to authenticate with.
    :type user: str
    :param password: The password to authenticate with.
    :type password: str
    :param vhost: The virtual host to use.
    :type vhost: str
    :param timeout: The timeout to use for blocking operations.
    :type timeout: float
    :param heartbeat: The heartbeat interval to use.
    :type heartbeat: int
    :param ssl: Whether to use SSL.
    :type ssl: bool
    :param ssl_options: SSL options to
