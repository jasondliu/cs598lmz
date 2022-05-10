import select
import socket
import sys
import time

from . import protocol
from . import exceptions
from . import util
from . import config
from . import logger

# Default timeout for socket operations
DEFAULT_SOCKET_TIMEOUT = 10

# Default timeout for the connection handshake
DEFAULT_HANDSHAKE_TIMEOUT = 10

# Default timeout for the connection handshake
DEFAULT_HANDSHAKE_RETRIES = 3

# The default port for the server to listen on
DEFAULT_PORT = 6667

# The default backlog for the server to listen with
DEFAULT_BACKLOG = 5

# The default size of the server's read buffer
DEFAULT_READ_BUFFER_SIZE = 4096

# The default size of the server's write buffer
DEFAULT_WRITE_BUFFER_SIZE = 4096

# The default size of the server's write buffer
DEFAULT_MAX_PACKET_SIZE = 4096

# The default size of the server's write buffer
DEFAULT_MAX_PACKETS_PER_SECOND = 10

# The default number of seconds to wait before
