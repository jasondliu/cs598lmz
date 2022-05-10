import select
import socket
import sys
import time
import threading
import traceback

from . import common
from . import config
from . import log
from . import util
from . import version

# The maximum number of bytes to read from a socket at a time.
_SOCKET_READ_SIZE = 1024

# The maximum number of bytes to write to a socket at a time.
_SOCKET_WRITE_SIZE = 1024

# The maximum number of bytes to read from a file at a time.
_FILE_READ_SIZE = 1024

# The maximum number of bytes to write to a file at a time.
_FILE_WRITE_SIZE = 1024

# The maximum number of bytes to read from a pipe at a time.
_PIPE_READ_SIZE = 1024

# The maximum number of bytes to write to a pipe at a time.
_PIPE_WRITE_SIZE = 1024

# The maximum number of bytes to read from a socket at a time when the socket is
# in non-blocking mode.
_SOCKET_READ_SIZE_NON_BLOCKING =
