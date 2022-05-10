import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect in thread
# ctypes.string_at return read-only memory:
#    ctypes.string_at(bytes, size)
#    Return a string containing the bytes in the byte string bytes.
#    size is the number of bytes to include in the string.

# ctypes.create_string_buffer return read-write memory:
#    ctypes.create_string_buffer(init, size)
#    Create a string buffer with the given initial value and size.
#    The buffer may hold up to size bytes, but the string itself can be longer.

# https://docs.python.org/3.5/library/threading.html
# The threading module constructs higher-level threading interfaces on top of
# the lower level _thread module.
# The threading module exposes all the methods of the _thread module and provides
# some additional methods. There is a difference between a thread’s identity
# and its name. A thread’s identity is a nonzero integer guaranteed to be unique
# and constant for the lifetime of the thread; this value is used in various places
# to identify a thread, including
