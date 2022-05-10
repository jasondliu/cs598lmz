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

def my_cb_1(p):
    a = my_threading_local.a
    return a.execute("select test(1, ?)", (1,)).fetchone()[0]

def my_cb_2():
    a = my_threading_local.a
    return a

def main():
    # Load the sqlite3 dll manually, so we can set sqlite3_open
    # appropriately.
    #
    # If we don't do this, then the wrong sqlite3_open will get used, which
    # will cause the db connection to fail.
    dllname = ctypes.util.find_library("sqlite3")
    if dllname is None:
        raise Exception("could not find sqlite3 library")
    dll = ctypes.CDLL(dllname)
    res = dll.sqlite3_open(DB_URI, ctypes.byref(ctypes.c_void_p()))
    assert res == 0

    uwsgi.register_rpc("test_rpc", my_cb)
