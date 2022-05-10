import select
import socket
import struct
import sys
import threading
import time

from contextlib import contextmanager

from . import _utils
from . import _common
from . import _constants
from ._common import _logger
from ._common import _set_socket_timeout

_logger = _utils.get_logger(__name__)

_BUF_SIZE = 1024

_DEFAULT_CONNECT_TIMEOUT = 10

_DEFAULT_TIMEOUT = 60

_DEFAULT_PING_INTERVAL = 10

_DEFAULT_RETRY_INTERVAL = 1

_DEFAULT_RECONNECT_INTERVAL = 1

_DEFAULT_PING_TIMEOUT = _DEFAULT_TIMEOUT - _DEFAULT_PING_INTERVAL

_DEFAULT_PING_RETRY = 3

_RETRY_INTERVAL = [0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4]

_RETRY_INTERVAL.extend([12.8] * 10)

