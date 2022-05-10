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
    a = my_threading_local.a

    assert a
    assert a.execute("select test(1, 2)").fetchone()[0] == 1
    assert a.execute("select test(10, 20)").fetchone()[0] == 10


def my_cb3(p):
    a = my_threading_local.a

    assert a

def my_cb6(p):
    a = my_threading_local.a

    assert a

def my_cb9(p):
    try:
        a = my_threading_local.a
        assert False, "my_threading_local.a should be deleted"
    except AttributeError:
        pass


if __name__ == "__main__":
    #load libsqlite3
    path = ctypes.util.find_library("sqlite3")
    sqlite3 = ctypes.CDLL(path)
    sqlite3_config = ctypes.CFUNCTYPE(None, ctypes.c_
