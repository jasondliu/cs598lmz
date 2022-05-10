import select
import socket
import sys
import threading
import time
import traceback

import pika

from . import common
from . import config
from . import log
from . import util

_logger = log.get_logger(__name__)


class _Connection(object):
    """
    A connection to a RabbitMQ server.

    This class is not thread-safe.
    """

    def __init__(self, host, port, user, password, virtual_host,
                 heartbeat_interval=None, connection_attempts=None,
                 retry_delay=None, socket_timeout=None):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._virtual_host = virtual_host
        self._heartbeat_interval = heartbeat_interval
