import select
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

__all__ = ['Client', 'Server']

logger = logging.getLogger(__name__)


class Client(object):
    """
    A client for the ZeroMQ Majordomo Protocol (MDP/0.2).

    This class implements the MDP/0.2 client side as described in
    http://rfc.zeromq.org/spec:7 and http://rfc.zeromq.org/spec:8.

    The client connects to a broker and sends requests. It then waits for
    replies.

    :param str broker: The address of the broker to connect to.
    :param str service: The name of the service to request.
    :param int timeout: The timeout in milliseconds to wait for replies.
    :param int retries: The number of times to retry a request before giving
        up.
    :param bool verbose: Whether to log debug information
