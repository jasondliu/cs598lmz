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

__all__ = ['Connection']

LOGGER = logging.getLogger(__name__)

#: The default timeout for socket operations.
DEFAULT_TIMEOUT = 30.0

#: The default size of the socket send buffer.
DEFAULT_SEND_BUFFER_SIZE = 65536

#: The default size of the socket receive buffer.
DEFAULT_RECV_BUFFER_SIZE = 65536

#: The default size of the socket send buffer.
DEFAULT_SEND_BUFFER_SIZE = 65536

#: The default size of the socket receive buffer.
DEFAULT_RECV_BUFFER_SIZE = 65536

#: The default size of the socket send buffer.
DEFAULT_SEND_BUFFER_SIZE = 65536

#: The default size of the socket receive buffer.
DEFAULT_RECV_BUFFER_SIZE = 65536

#: The default size of the
