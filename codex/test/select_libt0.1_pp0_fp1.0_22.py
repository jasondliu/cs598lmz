import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version

# pylint: disable=too-many-lines

# The maximum number of bytes to read from a socket at a time.
_SOCKET_READ_SIZE = 4096

# The maximum number of bytes to write to a socket at a time.
_SOCKET_WRITE_SIZE = 4096

# The maximum number of bytes to read from a file at a time.
_FILE_READ_SIZE = 4096

