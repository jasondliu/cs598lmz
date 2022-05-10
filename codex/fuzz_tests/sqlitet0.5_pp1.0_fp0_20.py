import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

# This is the function that will be called by the sqlite3_thread_cleanup()
# function.
def my_thread_cleanup():
    my_threading_local.a.close()

# Find the sqlite3 library.
lib = ctypes.util.find_library("sqlite3")

# Load the library.
lib = ctypes.CDLL(lib)

# Create the sqlite3_thread_cleanup() function.
lib.sqlite3_thread_cleanup.restype = None
lib.sqlite3_thread_cleanup.argtypes = None

# Create the sqlite3_shutdown() function.
lib.sqlite3_shutdown.restype = None
lib.sqlite3_shutdown.argtypes = None

# Create the sqlite3_initialize() function.
lib.sqlite3_initialize.restype = ctypes.c_int
lib.sqlite3_initialize.argtypes = None

# Create the sqlite3_config() function.
lib.sqlite3_config.restype = c
