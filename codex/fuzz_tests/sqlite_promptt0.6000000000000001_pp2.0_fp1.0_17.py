import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# Create a global connection to the database
conn = sqlite3.connect(':memory:')

# Create a global cursor for the database
cur = conn.cursor()

# Create a global lock for the database
lock = threading.Lock()

# Create a global variable for the library
_lib = None

# Load the library
def load_lib():
    global _lib
    if _lib is None:
        _lib = ctypes.CDLL(ctypes.util.find_library('zmq'))

    # Create a global zmq context
    global _zmq_context
    _zmq_context = _lib.zmq_ctx_new()

# ZeroMQ constants
ZMQ_PUB = 1
ZMQ_SUB = 2
ZMQ_SUBSCRIBE = 6
ZMQ_POLLIN = 1
ZMQ_POLLOUT = 2
ZMQ_POLLERR = 4
ZMQ_POLLPRI = 8

# Helper class for creating a ZeroMQ socket
class ZMQ
