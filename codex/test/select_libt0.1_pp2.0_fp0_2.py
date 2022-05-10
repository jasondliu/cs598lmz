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
from . import events
from . import log
from . import utils

# The maximum number of bytes to read from the socket at a time.
_MAX_READ_BYTES = 4096

# The maximum number of bytes to write to the socket at a time.
_MAX_WRITE_BYTES = 4096

# The maximum number of bytes to read from the socket at a time when
# reading a message.
_MAX_MESSAGE_READ_BYTES = 4096

# The maximum number of bytes to write to the socket at a time when
# writing a message.
_MAX_MESSAGE_WRITE_BYTES = 4096

# The maximum number of bytes to read from the socket at a time when
# reading a message header.
