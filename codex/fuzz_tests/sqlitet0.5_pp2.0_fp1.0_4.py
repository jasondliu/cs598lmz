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
    assert ctypes.util.find_library("sqlite3") is not None

    # load the sqlite3 library
    sqlite3_lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

    # register the callback
    sqlite3_lib.sqlite3_config(ctypes.c_int(2), my_cb, None)

    # create and delete a connection
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    del a

    # create another connection
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    # check that the user-defined function is still available
    a.execute("SELECT test(1, 2)")
    assert a.fetchone()[0] == 1

if __name__ == "__main__":
    main()
