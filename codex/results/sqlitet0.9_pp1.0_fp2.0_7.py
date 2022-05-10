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

class test_cb(object):
    def __init__(self):
        self.tested = False

    def __call__(self, p):
        self.tested = True
        return 1

my_cb = test_cb()

sqlite3.sqlite3_progress_handler(1, my_cb)

def main():
    cdll = None

    libs = ["libsqlite3.so"]
    for lib in libs:
        try:
            cdll = ctypes.CDLL(ctypes.util.find_library(lib))
            break
        except OSError:
            pass

    if not cdll:
        print("WARNING: could not find any sqlite3 libs :(")
        return

    a = sqlite3.connect(DB_URI, uri=True)

    with a:
        a.execute("create table test (foo int)")
        a.execute("insert into test (foo) values (0)")

        res = 0
        while res != 1:
            a.execute("insert into test (foo)
