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
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    lib.sqlite3_set_authorizer(lib.sqlite3_threadsafe(), my_cb_c, 0)

    a = sqlite3.connect(DB_URI, uri=True)

    a.execute("create table test(test varchar(1337))")
    a.commit()

    my_threading_local.a.execute("create table test(test varchar(1337))")
    my_threading_local.a.commit()

    # sqlite3.connect is called once more time here, but it leaks
    a.execute("select test(1, test) from test")
