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

class MyThread(threading.Thread):
    def run(self):
        conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        conn.execute('create table if not exists foo(a)')
        conn.execute('insert into foo values(?)', [1])
        conn.execute('select test(a, 2) from foo')

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.srand(libc.time(0) ^ libc.getpid())

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_initialize()

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_GETMALLOC, ctypes.byref(ctypes.c_void_p()))
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MALLOC, c
