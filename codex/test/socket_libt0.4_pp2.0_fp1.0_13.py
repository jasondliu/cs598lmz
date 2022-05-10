import socket
import ssl
import time
from datetime import datetime
import sys

from . import utils
from . import config
from . import constants
from . import exceptions
from . import logging
from . import __version__

logger = logging.getLogger(__name__)


class Client:
    """
    Client object for interacting with the API.
    """

    def __init__(self, host: str, port: int, username: str, password: str,
                 use_ssl: bool = True, verify_ssl: bool = True,
                 timeout: int = 10):
        """
        Initialize a new Client object.

        :param host: Hostname or IP address of the API server.
        :param port: Port to use for the connection.
        :param username: Username to authenticate with.
        :param password: Password to authenticate with.
        :param use_ssl: Whether to use SSL for the connection.
        :param verify_ssl: Whether to verify the SSL certificate.
        :param timeout: Timeout for the connection.
        """
