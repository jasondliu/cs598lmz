import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

#
# Python 2.x and 3.x compatibility
#

try:
    import queue
except ImportError:
    import Queue as queue

#
# Constants
#

#
# The maximum number of bytes to read from a socket at a time.
#
# This is used in the read loop for the control socket, to limit the amount of
# data read from the socket at a time.  It prevents the read operation from
# blocking for too long.
#
# The default is 16k.
#
MAX_CONTROL_LINE_LENGTH = 16384

#
# The maximum number of bytes to read from a socket at a time.
#
# This is used in the read loop for data sockets, to limit the amount of data
# read from the socket at a time.  It prevents the read operation from blocking
# for too long.
#
# The default is 64k.
#
MAX_DATA_RECV_LENGTH = 65536

#
# The number of seconds to wait for a connection to be established.
#
# This is used
