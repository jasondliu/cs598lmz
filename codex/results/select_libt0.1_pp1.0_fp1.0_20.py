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

logger = log.get_logger(__name__)

# The maximum number of bytes to read from a socket at a time.
MAX_READ = 65536

# The number of seconds to wait for a socket to become readable or writable.
SELECT_TIMEOUT = 1.0

# The number of seconds to wait for a socket to become readable or writable
# when we're expecting a response.
SELECT_TIMEOUT_SHORT = 0.1

# The number of seconds to wait for a socket to become readable or writable
# when we're expecting a response.
SELECT_TIMEOUT_LONG = 10.0

# The number of seconds to wait for a socket to become readable or writable
# when we're expecting a response.
SELECT_TIMEOUT_VERY_LONG = 60.0

# The number of seconds to wait for a socket to become readable or writable
# when we're expecting a response.
SELECT
