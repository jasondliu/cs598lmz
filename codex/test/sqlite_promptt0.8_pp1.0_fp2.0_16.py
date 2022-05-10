import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import time

class TUI_Server(threading.Thread):

    # This is the theoretical maximum number of connections that can be
    # supported on most systems.  (Most systems impose limits on the
    # number of open file descriptors that are lower than this number.)
    # With this value there is no need to have a separate maximum
    # connection count parameter.
    _MAX_CONNECTIONS = 128

    # The number of I/O threads to create in each I/O completion port.
    _NUM_IO_THREADS = 2

    # A simple linked-list structure for tracking connected clients.
    class Client(ctypes.Structure):
        _fields_ = [('next', ctypes.c_void_p),
                    ('socket', ctypes.c_int),
                    ('addr', ctypes.c_char * 28),
                    ('port', ctypes.c_ushort)]

    # A simple linked-list structure for tracking events that are
    # ready to be processed.
