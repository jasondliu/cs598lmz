import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import crypto
from . import database
from . import log
from . import message
from . import network
from . import protocol
from . import util

# The maximum number of bytes to read from a socket at once.
_MAX_READ_BYTES = 4096

# The maximum number of bytes to write to a socket at once.
_MAX_WRITE_BYTES = 4096

# The maximum number of bytes to read from a socket at once when reading a
# message.
_MAX_MESSAGE_READ_BYTES = 4096

# The maximum number of bytes to write to a socket at once when writing a
# message.
_MAX_MESSAGE_WRITE_BYTES = 4096

# The maximum number of bytes to read from a socket at once when reading a
# message header.
_MAX_MESSAGE_HEADER_READ_BYTES = 4096

# The maximum number of bytes to write to a socket
