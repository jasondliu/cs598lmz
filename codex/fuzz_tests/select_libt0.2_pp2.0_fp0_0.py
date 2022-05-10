import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import logger
from . import utils
from . import version

_log = logger.get_logger(__name__)


class Client(object):
    """
    Client class for interacting with the server.

    :param host: Hostname or IP address of the server.
    :type host: str
    :param port: Port of the server.
    :type port: int
    :param timeout: Timeout for socket operations.
    :type timeout: int
    :param ssl: Use SSL for the connection.
    :type ssl: bool
    :param ssl_verify: Verify the SSL certificate.
    :type ssl_verify: bool
    :param ssl_cert: Path to the SSL certificate.
    :type ssl_cert: str
    :param ssl_key: Path to the SSL key.
    :type ssl_key: str
    :param ssl_ca: Path to the CA certificate.
    :type
