import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version

# The default timeout for a socket.
DEFAULT_SOCKET_TIMEOUT = 30

# The default timeout for a socket.
DEFAULT_SOCKET_CONNECT_TIMEOUT = 5

# The default timeout for a socket.
DEFAULT_SOCKET_READ_TIMEOUT = 60

# The default timeout for a socket.
DEFAULT_SOCKET_WRITE_TIMEOUT = 60

# The default timeout for a socket.
DEFAULT_SOCKET_KEEPALIVE = 1

# The default timeout for a socket.
DEFAULT_SOCKET_KEEPALIVE_OPTIONS = (
    socket.TCP_KEEPIDLE,
    socket.TCP_KEEPINTVL,
    socket.TCP_KEEPCNT,
)

# The default timeout for a socket.
