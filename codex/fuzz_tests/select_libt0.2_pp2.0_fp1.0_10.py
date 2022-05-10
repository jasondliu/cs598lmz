import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import log
from . import util
from . import version

# The following are used for the server-side of the protocol.

# The server's socket.
server_socket = None

# The server's listening thread.
server_thread = None

# The server's listening port.
server_port = None

# The server's listening address.
server_address = None

# The server's listening backlog.
server_backlog = None

# The server's listening timeout.
server_timeout = None

# The server's listening socket timeout.
server_socket_timeout = None

# The server's listening socket address family.
server_address_family = None

# The server's listening socket type.
server_socket_type = None

# The server's listening socket protocol.
server_socket_protocol = None

# The server's listening socket.
server_listening_socket = None

# The server's listening socket file descriptor.
server_
