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
from . import log
from . import messages
from . import protocol
from . import util
from . import version

logger = log.get_logger(__name__)


class Client(object):
    """
    A client for the NATS messaging system.

    :param servers: List of servers to connect to.
    :type servers: list(str)
    :param str user: Optional user name for authentication.
    :param str password: Optional password for authentication.
    :param str name: Optional client name.
    :param bool verbose: True to enable verbose logging.
    :param bool pedantic: True to enable pedantic logging.
    :param bool allow_reconnect: True to allow reconnection.
    :param int max_reconnect_attempts: Maximum number of reconnect attempts.
    :param float reconnect_time_wait: Time to wait between reconnect attempts.
    :param io_loop: Optional Tornado IOL
