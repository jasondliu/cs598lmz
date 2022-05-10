import select
import socket
import sys
import threading
import time
import traceback

from . import __version__
from . import constants
from . import exceptions
from . import utils
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_socket_timeout = 5
_g_socket_timeout_long = 60
_g_socket_timeout_long_long = 600
_g_socket_timeout_long_long_long = 3600
_g_socket_timeout_long_long_long_long = 3600 * 24

_g_socket_timeout_long_long_long_long_long = 3600 * 24 * 7

_g_socket_timeout_short = 0.5
_g_socket_timeout_short_short = 0.1

_g_socket_timeout_short_short_short = 0.01

_g_socket_timeout_short_short_short_short = 0.001

