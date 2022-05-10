import select
import socket
import sys
import threading
import time
import traceback

import pika
import pika.exceptions
import pika.spec

from . import compat
from . import exceptions
from . import spec

# pylint: disable=too-many-instance-attributes,too-many-public-methods

LOGGER = logging.getLogger(__name__)


class Connection(object):
    """This is the main class for communicating with RabbitMQ.

    It's responsible for managing the connection to RabbitMQ,
    including establishing the connection, closing it, and re-establishing
    it if it's closed unexpectedly.

    It also provides methods for creating new channels, and closing them
    when they're no longer needed.

    :param pika.connection.Parameters parameters: Connection parameters
    :param bool custom_ioloop: Use a custom IOLoop instance
    :param on_open_callback: The method to call when the connection is open
    :type on_open_callback: method
    :param on_open_error_callback: The method to call if the connection cant

