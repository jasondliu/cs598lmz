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

def main():
    global my_threading_local

    # This test assumes that no other threading-related operations have
    # been performed on this thread, and that no other threads are
    # currently running.

    # Load the SQLite library
    sqlite_lib = ctypes.util.find_library('sqlite3')
    if not sqlite_lib:
        print '\n*** sqlite3 library not found ***\n'
        return

    lib = ctypes.CDLL(sqlite_lib)

    # Make sure we have a threading-capable version of SQLite
    lib.sqlite3_threadsafe.restype = ctypes.c_int
    if lib.sqlite3_threadsafe() == 0:
        print '\n*** sqlite3 is not thread-safe ***\n'
        return

    # Set the threading mode
    lib.sqlite3_config(ctypes.c_int(2))

    # Register the callback
    lib.sqlite3_initialize()
    lib.sqlite3_shutdown.argtypes = []
