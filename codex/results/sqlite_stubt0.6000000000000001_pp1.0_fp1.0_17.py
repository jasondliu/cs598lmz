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
    # Load the sqlite shared library
    ctypes.CDLL(ctypes.util.find_library('sqlite3'))

    # Initialize the sqlite threading.
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

    # Initialize the sqlite connection.
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    # Creates a "threading-safe" user-defined function.
    a.create_function("thread_init", 0, my_cb)

    # This will cause a new thread to be created and the my_cb function to be called.
    a.execute("SELECT * FROM sqlite_master;")

    # This will cause the thread to be released.
    a.close()

    # Release the memory for the sqlite3_vfs object.
    sqlite3.sqlite3_vfs_unregister(sqlite3.sqlite3_vfs_find("main"))

    # The memory for the
