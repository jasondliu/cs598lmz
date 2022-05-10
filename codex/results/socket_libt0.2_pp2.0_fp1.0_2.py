import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version
from . import __version__
from . import __author__
from . import __license__
from . import __copyright__

logger = logging.getLogger(__name__)


class Client(object):
    """
    Client class for connecting to the server.

    :param str host: Hostname or IP address of the server.
    :param int port: Port of the server.
    :param str username: Username to use for authentication.
    :param str password: Password to use for authentication.
    :param str client_id: Client ID to use for authentication.
    :param bool ssl: Use SSL for the connection.
    :param int timeout: Timeout in seconds for the connection.
    :param int keepalive: Keepalive in seconds for the connection.
    :param bool clean_session: Clean session flag for the connection.
    :param bool session_expiry: Session expiry interval in seconds for the connection.

