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

#
# Constants
#

# The maximum number of bytes to read from a socket at a time.
MAX_READ_SIZE = 4096

# The maximum number of bytes to write to a socket at a time.
MAX_WRITE_SIZE = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a line.
MAX_LINE_SIZE = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a request.
MAX_REQUEST_SIZE = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a response.
MAX_RESPONSE_SIZE = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a response body.
MAX_BODY_SIZE = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a response body chunk.
MAX
