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
    assert a.execute("SELECT test(1, 2)").fetchone()[0] == 1
    del my_threading_local.a

def my_cb_init(p):
    pass

def my_cb_shutdown(p):
    pass

def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) != 2:
        print 'Usage: %s <sqlite-lib-file>' % argv[0]
        return 1

    libsqlite = ctypes.CDLL(argv[1])
    if not libsqlite:
        print 'Cannot load %s' % argv[1]
        return 1

    libsqlite.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
    libsqlite.sqlite3_open.restype = ctypes.c
