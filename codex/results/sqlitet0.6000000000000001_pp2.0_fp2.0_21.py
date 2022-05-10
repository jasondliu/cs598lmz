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

def my_cb2(a, b):
    return 1

alpha = ctypes.CDLL(ctypes.util.find_library('c'))
p = alpha.malloc(100)
alpha.free(p)

sqlite3.enable_callback_tracebacks(True)

sqlite3.set_authorizer(my_cb)
sqlite3.set_authorizer(my_cb2)

# Causes the bug
conn = sqlite3.connect(DB_URI, uri=True)

# Causes a SIGSEGV
conn.execute('select test(?)', (1,))

# Causes a SIGSEGV
conn.execute('select test(?)', (1,))

conn.close()

# Causes a SIGSEGV
conn = sqlite3.connect(DB_URI, uri=True)
conn.close()
