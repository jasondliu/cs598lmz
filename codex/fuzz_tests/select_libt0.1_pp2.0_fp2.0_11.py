import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version

# The maximum number of bytes to read from a socket at a time.
_MAX_READ_BYTES = 1024

# The maximum number of bytes to write to a socket at a time.
_MAX_WRITE_BYTES = 1024

# The maximum number of bytes to read from a socket at a time when reading
# a message.
_MAX_MESSAGE_READ_BYTES = 1024

# The maximum number of bytes to write to a socket at a time when writing
# a message.
_MAX_MESSAGE_WRITE_BYTES = 1024

# The maximum number of bytes to read from a socket at a time when reading
# a message header.
_MAX_MESSAGE_HEADER_READ_BYTES = 1024

# The maximum number of bytes to write to a socket at a time when writing
# a message header.
_MAX_MESSAGE_HEADER_WRITE
