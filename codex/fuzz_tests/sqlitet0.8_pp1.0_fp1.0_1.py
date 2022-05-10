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

    a.close()

    return 1

def my_cb3(p):
    a = my_threading_local.a

    a.cursor().execute("select test(?, ?)", (1, 2))

    return 1

def init():
    lib = ctypes.CDLL(ctypes.util.find_library("pthread"))
    lib.pthread_atfork(my_cb, my_cb2, my_cb3)

def insert_thread():
    a = my_threading_local.a

    a.cursor().execute("insert into test(n, n2) values(3, 4)")

def check_thread():
    a = my_threading_local.a

    a.cursor().execute("select * from test")

    assert list(a.cursor().fetchall()) == [(3, 4)]


if __name__ == '__main__':
    init()
    sqlite3.threadsafety = 2

    a
