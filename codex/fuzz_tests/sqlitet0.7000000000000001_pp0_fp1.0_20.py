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


pysqlite_connection_hook = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

lib = ctypes.util.find_library("sqlite3")

CTX = ctypes.c_void_p.in_dll(ctypes.CDLL(lib), "sqlite3_vfs").value
CTX = ctypes.cast(CTX, ctypes.c_void_p)


ctypes.cdll.LoadLibrary(lib).sqlite3_vfs_register(pysqlite_connection_hook, 1)

a = sqlite3.connect(DB_URI, uri=True)

print(a.execute("select test(?);", ("test",)).fetchall())

print(my_threading_local.a.execute("select test(?);", ("test",)).fetchall())
</code>

