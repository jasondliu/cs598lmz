import select
import socket
import sys
import threading
import time

import pika
import pika.exceptions

from . import exceptions
from . import spec
from . import utils


class ConnectionParameters(object):
    """
    This class is used to pass connection parameters to the Connection
    constructor.

    :param str host: Hostname or IP address to connect to.
    :param int port: Port number to connect on.
    :param str virtual_host: Virtual host to use.
    :param str credentials: Credentials to use.
    :param bool ssl: Use SSL.
    :param dict client_properties: Connection properties to use.
    :param int frame_max: Maximum frame size.
    :param int heartbeat: Heartbeat interval.
    :param int retry_delay: Time to wait before retrying a connection.
    :param int socket_timeout: Timeout for blocking operations.
    :param int shutdown_timeout: Timeout for graceful shutdown.
    :param bool locale: Locale to use.
    :param bool backpressure_detection: Enable backpressure detection.
    :
