import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import utils
from . import version

# This is the default port that the server listens on.
DEFAULT_PORT = 6667

# This is the default backlog for the server socket.
DEFAULT_BACKLOG = 5

# This is the default timeout for the server socket.
DEFAULT_TIMEOUT = 60

# This is the default maximum number of connections.
DEFAULT_MAX_CONNECTIONS = 100

# This is the default maximum number of connections per IP.
DEFAULT_MAX_CONNECTIONS_PER_IP = 5

# This is the default maximum number of connections per IP.
DEFAULT_MAX_CONNECTIONS_PER_IP_PER_SECOND = 1

# This is the default maximum number of connections per IP.
DEFAULT_MAX_CONNECTIONS_PER_IP_PER_MINUTE = 5

# This is the default maximum number of connections per IP.
