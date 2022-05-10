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
    A connection to a remote server.

    :param host: The host to connect to.
    :type host: str

    :param port: The port to connect to.
    :type port: int

    :param user: The username to authenticate with.
    :type user: str

    :param password: The password to authenticate with.
    :type password: str

    :param database: The database to connect to.
    :type database: str

    :param timeout: The timeout in seconds before the connection attempt fails.
    :type timeout: int

    :param ssl: Use SSL to connect to the server.
    :type ssl: bool

    :param verify_ssl: Verify the SSL certificate.
    :type verify_ssl: bool

    :param ssl_options: SSL options to
