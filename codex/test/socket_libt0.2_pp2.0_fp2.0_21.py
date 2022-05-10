import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version

# The default port to use for the HTTP server.
DEFAULT_PORT = 8080

# The default host to use for the HTTP server.
DEFAULT_HOST = '0.0.0.0'

# The default number of seconds to wait before timing out a request.
DEFAULT_TIMEOUT = 60

# The default number of seconds to wait before timing out a request.
DEFAULT_MAX_REQUEST_SIZE = 1024 * 1024 * 10

# The default number of seconds to wait before timing out a request.
DEFAULT_MAX_REQUEST_HEADER_SIZE = 1024 * 1024

# The default number of seconds to wait before timing out a request.
DEFAULT_MAX_REQUEST_HEADER_COUNT = 100

# The default number of seconds to wait before timing out a request.
DEFAULT_MAX_REQUEST_LINE_SIZE = 8192

# The default number of seconds to wait before timing out a request.
DE
