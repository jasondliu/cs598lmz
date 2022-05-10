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

def my_cb2(p):
    my_threading_local.a.close()
    return 1

if __name__ == '__main__':
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_initialize()
    lib.sqlite3_config(1, 1)

    # Set up a connection to a database, create a table and a function
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("CREATE TABLE test (a, b)")
    a.execute("INSERT INTO test VALUES (1, 2)")
    a.execute("INSERT INTO test VALUES (3, 4)")
    a.commit()

    # Register a callback to be called when a connection is opened
    lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c
