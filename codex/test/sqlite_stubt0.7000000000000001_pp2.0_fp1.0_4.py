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

def test_sqlite_threading():
    # load the SQLite library
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    # define the callback function
    cb = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

    # set the callback function
    lib.sqlite3_set_authorizer(cb)

    # open the database
    conn = sqlite3.connect(DB_URI, uri=True)

    thread = threading.Thread(target=conn.execute,
        args=("select * from test where test(?, ?)", (1, 2)))
    thread.start()
    thread.join()

    assert my_threading_local.a.execute("select test(?, ?)", (1, 2)).fetchall() == [(1,)]
