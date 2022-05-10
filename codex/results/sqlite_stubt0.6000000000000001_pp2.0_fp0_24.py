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

if __name__ == '__main__':
    # Initialize the threading system
    sqlite3.threadsafety = 2
    sqlite3.enable_callback_tracebacks(True)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    if lib.sqlite3_config(ctypes.c_int(4)) != 0:
        raise Exception("sqlite3_config failed")

    # Set the threading mode
    lib.sqlite3_config(ctypes.c_int(1), ctypes.c_int(1))

    # Register the callback
    lib.sqlite3_initialize()
    lib.sqlite3_shutdown()

    callback = sqlite3.SQLiteThreadingCallback(my_cb)

    # Initialize the threading system
    sqlite3.threadsafety = 2
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_threading_callback(callback)

    # Create the main connection
    main_conn = sqlite3.connect(DB
