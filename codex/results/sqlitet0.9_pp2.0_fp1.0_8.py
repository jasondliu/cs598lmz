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

sqlite3.sqlite3_prepare_hint = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t)(my_cb)

def my_init(f):
    sqlite3._sqlite.__init__(f)
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_prepare_hint(b"test", len(b"test"))

sqlite3._sqlite.__init__ = my_init

def test():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a + b

    conn.create_function("test", 2, test_fn)

    cur = conn.cursor()
    cur.execute('''SELECT test(?, ?)''', (1,2))
    assert cur.fetchall() == [(3,)]

    my_thread
