import select
import socket
import sys
import threading
import time

from . import config
from . import constants
from . import errors
from . import events
from . import logger
from . import utils
from . import version
from .logger import Logger
from .utils import get_ip_address


class Server:
    """
    Server class.

    :param str host: Hostname or IP address to listen on.
    :param int port: Port to listen on.
    :param int backlog: Number of connections to allow in backlog.
    :param int timeout: Timeout for client connections.
    :param int max_connections: Maximum number of simultaneous connections.
    :param int max_clients: Maximum number of clients.
    :param int max_messages: Maximum number of messages.
    :param int max_payload: Maximum payload size.
    :param bool debug: Enable debug mode.
    :param bool udp: Enable UDP mode.
    :param bool ipv6: Enable IPv6 mode.
    :param bool tls: Enable TLS mode.
    :param bool tls_required
