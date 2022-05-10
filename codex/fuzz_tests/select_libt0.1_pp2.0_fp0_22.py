import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import protocol
from . import util
from . import version

# The default timeout for socket operations.
DEFAULT_SOCKET_TIMEOUT = 30

# The default timeout for connect operations.
DEFAULT_CONNECT_TIMEOUT = 30

# The default timeout for read operations.
DEFAULT_READ_TIMEOUT = 30

# The default timeout for write operations.
DEFAULT_WRITE_TIMEOUT = 30

# The default timeout for wait operations.
DEFAULT_WAIT_TIMEOUT = 30

# The default timeout for close operations.
DEFAULT_CLOSE_TIMEOUT = 30

# The default timeout for open operations.
DEFAULT_OPEN_TIMEOUT = 30

# The default timeout for flush operations.
DEFAULT_FLUSH_TIMEOUT = 30

# The default timeout for shutdown operations.
DEFAULT_SHUTDOWN_TIMEOUT = 30

# The default timeout for accept operations.
DEFAULT_ACCEPT_TIMEOUT = 30


