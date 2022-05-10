import socket
import sys
import threading
import time

from pybase import pylog, pybase

pybase.check_py_version()

# Default timeout for socket operations.
_DEFAULT_TIMEOUT = 5.0

# Used internally to indicate that the socket should be closed.
_SHUTDOWN_SOCKET = -1

# Used internally to indicate that the socket should be closed.
_SHUTDOWN_SOCKET_WITH_PID = -2

# Used internally to indicate that the socket should be closed.
_SHUTDOWN_SOCKET_WITH_SIZE = -3

# The size of the string we send to a server before we close the connection.
_SHUTDOWN_STRING_SIZE = 128

# The port we use for the server.
_DEFAULT_PORT = 9999

# The size of the string we send to a server before we close the connection.
_DEFAULT_MESSAGE_SIZE = 128

# The size of the string we send to a server before we close the connection.
_DEFAULT_MESSAGE_NUM
