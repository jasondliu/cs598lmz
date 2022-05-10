import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import util
from . import version

#
# Constants
#

# The maximum number of bytes to read from a socket at a time.
MAX_READ = 4096

# The maximum number of bytes to write to a socket at a time.
MAX_WRITE = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a line.
MAX_LINE = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a request.
MAX_REQUEST = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a response.
MAX_RESPONSE = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a response body.
MAX_BODY = 4096

# The maximum number of bytes to read from a socket at a time when
# reading a response body chunk.
MAX_CHUNK = 4096

# The maximum number of bytes to read
