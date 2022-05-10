import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import protocol
from . import utils
from . import version

__all__ = ['Client']

logger = logging.getLogger(__name__)


class Client(object):
    """
    A client for the NATS messaging system.

    :param str servers: A list of servers to connect to.
    :param str username: The username to use for authentication.
    :param str password: The password to use for authentication.
    :param str token: The token to use for authentication.
    :param str name: The name of the client.
    :param bool verbose: Enable verbose logging.
    :param bool pedantic: Enable pedantic logging.
    :param bool allow_reconnect: Allow the client to reconnect.
    :param int max_reconnect_attempts: The maximum number of reconnect attempts.
    :param float reconnect_time_wait: The time to wait between reconnect attempts.
    :param float ping_interval: The interval to send ping messages.
