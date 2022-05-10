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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open(DB_URI.encode("ascii"), ctypes.pointer(ctypes.c_void_p()))
lib.sqlite3_enable_load_extension(
    ctypes.c_void_p(), 1
)
lib.sqlite3_load_extension(
    ctypes.c_void_p(), b"test.so", b"test_init", ctypes.pointer(ctypes.c_int())
)

my_threading_local.a.execute("select * from test_table")
</code>
When I run this I get a segmentation fault.  However, if I replace the last two lines with:
<code>a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("select * from test_table")
</code>
it works.  If I replace the last two lines with:
<code>my_threading_local
