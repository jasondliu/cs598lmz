import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import xlog

_logger = log.get_logger(__name__)

# The maximum amount of data to read at once.
_MAX_READ = 4096

# The maximum amount of data to write at once.
_MAX_WRITE = 4096

# The maximum number of connections to accept at once.
_MAX_ACCEPT = 10

# The maximum number of connections to poll at once.
_MAX_POLL = 10

# The maximum number of connections to process at once.
_MAX_PROCESS = 10

# The maximum number of connections to close at once.
_MAX_CLOSE = 10

# The maximum number of connections to close at once.
_MAX_CLOSE = 10

# The maximum number of connections to close at once.
_MAX_CLOSE = 10

# The maximum number of connections to close at once.
_MAX_CLOSE = 10

# The maximum number of connections to close at once.

