import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import constants
from . import exceptions
from . import protocol
from . import util
from . import version

log = logging.getLogger(__name__)

#: The default port to connect to.
DEFAULT_PORT = constants.DEFAULT_PORT

#: The default host to connect to.
DEFAULT_HOST = constants.DEFAULT_HOST

#: The default timeout for socket operations.
DEFAULT_TIMEOUT = constants.DEFAULT_TIMEOUT

#: The default amount of time to wait for a connection to be established.
DEFAULT_CONNECT_TIMEOUT = constants.DEFAULT_CONNECT_TIMEOUT

#: The default amount of time to wait for a connection to be established.
DEFAULT_RECONNECT_TIMEOUT = constants.DEFAULT_RECONNECT_TIMEOUT

#: The default amount of time to wait for a connection to be established.
DEFAULT_RECONNECT_DELAY = constants.DEFAULT_RECONNECT_DELAY
