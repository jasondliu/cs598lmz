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
    b = my_threading_local.a
    return 1

sqlite3.sqlite3_initialize()

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
lib.sqlite3_shutdown.restype = ctypes.c_int
lib.sqlite3_shutdown.argtypes = []

lib.sqlite3_config(ctypes.c_int(3), my_cb, my_cb2)

a = sqlite3.connect(DB_URI, uri=True)

a.execute("SELECT test(?);", ("test",))

lib.sqlite3_shutdown()
</code>
When I run the above code, I get the following error:
<code>ProgrammingError: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 5144 and this is thread id 7052
</code>
How do I use the <code>sqlite3</code> library functions in a callback that is only
