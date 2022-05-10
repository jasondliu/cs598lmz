import select
import socket
import sys
import time

from . import base
from . import compat
from . import errors
from . import util
from . import event

__all__ = ["TCPClient"]

# Read buffer size for socket.recv()
_READ_BUFFER_SIZE = 8192

# Timeout for socket.recv()
_READ_TIMEOUT = 1.0

# Default number of seconds to wait for the next connection attempt
_RETRY_INTERVAL = 1.0

# Default number of seconds to wait for the next read attempt
_READ_RETRY_INTERVAL = 0.1

# Size of the write buffer
_WRITE_BUFFER_SIZE = 8192

# Timeout for socket.send()
_WRITE_TIMEOUT = 1.0

# Default number of seconds to wait for the next write attempt
_WRITE_RETRY_INTERVAL = 0.1

# Default number of seconds to wait for the next write attempt
_CLOSE_RETRY_INTERVAL = 0.1

# Number of seconds to wait for the next write attempt when the connection is
