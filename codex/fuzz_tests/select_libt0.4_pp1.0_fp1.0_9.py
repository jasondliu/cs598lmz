import selectors
import sys
import types
import logging
import logging.handlers

from . import config
from . import dispatcher
from . import exceptions
from . import protocol
from . import util

logger = logging.getLogger(__name__)


class BaseClient(object):
    """Base class for all clients.

    :param str host: The host to connect to.
    :param int port: The port to connect to.
    :param str username: The username to authenticate with.
    :param str password: The password to authenticate with.
    :param int timeout: The timeout in seconds to wait for a response.
    :param bool auto_reconnect: Whether or not to reconnect automatically.
    :param int max_reconnect_attempts: The maximum number of reconnection
        attempts.
    :param float reconnect_wait_seconds: The number of seconds to wait between
        reconnection attempts.
    :param float reconnect_wait_jitter: The amount of jitter to add to
        reconnect_wait_seconds.
    :param bool reconnect_wait_exponential_multiplier: The amount
