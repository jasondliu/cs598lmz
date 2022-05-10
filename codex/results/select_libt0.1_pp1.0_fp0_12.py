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
MAX_READ = 1024

# The maximum number of bytes to write to a socket at a time.
MAX_WRITE = 1024

# The maximum number of bytes to read from a socket at a time when
# reading the HTTP request.
MAX_REQUEST_READ = 1024

# The maximum number of bytes to read from a socket at a time when
# reading the HTTP response.
MAX_RESPONSE_READ = 1024

# The maximum number of bytes to write to a socket at a time when
# writing the HTTP request.
MAX_REQUEST_WRITE = 1024

# The maximum number of bytes to write to a socket at a time when
# writing the HTTP response.
MAX_RESPONSE_WRITE = 1024

# The maximum number of bytes to read from a socket at a time when
# reading the HTTP request body.
MAX_REQUEST_B
