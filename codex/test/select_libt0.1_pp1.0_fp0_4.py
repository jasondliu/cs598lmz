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
from . import utils

_logger = log.get_logger(__name__)


class Server(object):
    """
    A server that listens for connections from clients.

    :param config: The server configuration.
    :type config: :class:`~.config.ServerConfig`
    :param handler: The handler for incoming messages.
    :type handler: :class:`~.handler.Handler`
    """

