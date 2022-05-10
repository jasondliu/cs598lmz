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

sqlite3.enable_callback_tracebacks()

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
lib.sqlite3_enable_load_extension(None, 1)
lib.sqlite3_load_extension(None, b"lib.so", b"sqlite3_init", 0)
conn = sqlite3.connect(DB_URI, uri=True)
conn.execute("pragma query_only = 1")
conn.execute("select my_load_extension(%d)" % sys.getcheckinterval())

for i in range(100):
    my_threading_local.a.execute("select test(?, ?)", (1, 2))

