import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import log
from . import util

# The maximum number of bytes to read from a socket at a time.
MAX_READ_SIZE = 1024

# The maximum number of bytes to write to a socket at a time.
MAX_WRITE_SIZE = 1024

# The maximum number of bytes to read from a socket at a time when reading
# a message.
MAX_MESSAGE_READ_SIZE = 1024

# The maximum number of bytes to write to a socket at a time when writing
# a message.
MAX_MESSAGE_WRITE_SIZE = 1024

# The maximum number of bytes to read from a socket at a time when reading
