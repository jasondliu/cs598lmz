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

# The default port to listen on.
DEFAULT_PORT = config.get_config().getint('server', 'port')

# The default host to listen on.
DEFAULT_HOST = config.get_config().get('server', 'host')

# The default backlog for the server socket.
DEFAULT_BACKLOG = config.get_config().getint('server', 'backlog')

# The default timeout for the server socket.
DEFAULT_TIMEOUT = config.get_config().getint('server', 'timeout')

# The default maximum number of connections.
DEFAULT_MAX_CONNECTIONS = config.get_config().getint('server', 'max_connections')

# The default maximum number of threads.
DEFAULT_MAX_THREADS = config.get_config().getint('server', 'max_threads')

# The default maximum number of threads.
DEFAULT_MAX_REQU
