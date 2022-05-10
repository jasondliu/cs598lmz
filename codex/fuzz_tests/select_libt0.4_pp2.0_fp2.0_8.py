import select
import socket
import sys
import threading
import time
import traceback

from . import connection
from . import constants
from . import exceptions
from . import message
from . import utils

LOGGER = logging.getLogger(__name__)

class ConnectionManager(object):
    """
    Manages a single connection to the server.

    :param host: The hostname to connect to.
    :param port: The port to connect to.
    :param username: The username to authenticate with.
    :param password: The password to authenticate with.
    :param ssl: Whether to use SSL when connecting.
    :param ssl_options: A dictionary of options to pass to the SSL context.
    :param timeout: The timeout to use when connecting.
    :param keepalive: The keepalive interval to use.
    :param keepalive_max_missed: The maximum number of keepalive packets to
        miss before disconnecting.
    :param keepalive_response_timeout: The maximum time to wait for a response
        to a keepalive packet.
   
