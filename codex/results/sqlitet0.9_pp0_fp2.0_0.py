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

sqlite3.sqlite3_enable_load_extension(1)
c = sqlite3.connect(':memory:', uri=True, factory=deleting_conn)
#f = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
f = ctypes.cdll.LoadLibrary("/usr/lib64/libsqlite3.so.0")

res = f.sqlite3_enable_load_extension(c._handle, 1)

#f.sqlite3_close.argtypes = [ctypes.c_void_p]
res = f.sqlite3_load_extension(c._handle, "./helloExtension.so", 0, 0)

c.create_function("hello", 1, my_cb)
c.execute("select hello(5)")

del c

print( "End" )
