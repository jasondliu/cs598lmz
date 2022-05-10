import select
import socket
import sys
import threading
import time

from . import config
from . import constants
from . import errors
from . import log
from . import utils
from . import version

# pylint: disable=too-many-lines

# The following are used to determine the maximum number of bytes to read
# from a socket at a time.
_SOCKET_BUFFER_SIZE = 1024
_SOCKET_BUFFER_SIZE_MAX = 65536
_SOCKET_BUFFER_SIZE_MIN = 128
_SOCKET_BUFFER_SIZE_STEP = 128

# The following are used to determine the maximum number of bytes to read
# from a file at a time.
_FILE_BUFFER_SIZE = 1024
_FILE_BUFFER_SIZE_MAX = 65536
_FILE_BUFFER_SIZE_MIN = 128
_FILE_BUFFER_SIZE_STEP = 128

# The following are used to determine the maximum number of bytes to read
# from a pipe at a time.
_PIPE_BUFFER_SIZE = 1024
