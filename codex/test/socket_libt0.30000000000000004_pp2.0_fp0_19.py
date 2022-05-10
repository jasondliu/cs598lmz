import socket
import sys
import time
import threading

from . import constants
from . import exceptions
from . import utils
from . import version
from . import __version__
from . import logger

log = logger.get_logger(__name__)


class Connection(object):
    """
    A connection to a Riak TS node.

    :param str host: The hostname of the Riak TS node.
    :param int port: The protocol buffer port of the Riak TS node.
    :param float timeout: The socket timeout in seconds.
    :param str ca_cert: The path to the CA certificate.
    :param str client_cert: The path to the client certificate.
    :param str client_key: The path to the client key.
    :param bool verify: Whether to verify the server's certificate.
    :param str username: The username for basic auth.
    :param str password: The password for basic auth.
    """
