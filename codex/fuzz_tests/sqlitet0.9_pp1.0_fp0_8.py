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

f = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_commit_hook
f.argtypes = [ctypes.c_void_p]
f.restype = ctypes.c_int
f.errcheck = lambda x, f, args: x if x == 1 else 0

f.__call__(ctypes.c_void_p(-1))
print(my_threading_local.a.execute('select * from test').fetchall())
</code>
From within my C extension, I am executing a simple <code>select * from table</code> and calling a function registered via <code>sqlite3_create_function()</code>. The purpose of this query is to refresh the data in the table whenever it is committed to and since those functions are not called from the main thread (nor are they called from a thread that was explicitly spawned), they need to be re-registered.
The important things to notice are the use of <code>sqlite3_commit_hook</code> and <code>my_cb</code>. These are the two functions
