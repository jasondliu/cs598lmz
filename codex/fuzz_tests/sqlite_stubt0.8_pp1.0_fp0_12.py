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

p = sqlite3.sqlite_version_info
p = ctypes.c_void_p(ctypes.cast(ctypes.pointer(p), ctypes.c_void_p).value)

sqlite3.sqlite3_config(1, 1)
sqlite3.sqlite3_config(2, 1)
sqlite3.sqlite3_config(3, ctypes.addressof(sqlite3.sqlite3_shutdown))
sqlite3.sqlite3_initialize()

try:
    sqlite3.sqlite3_config(5, my_cb, p)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    return_value = a.execute('SELECT test(1, 2)').fetchall()[0][0]

    assert return_value == 1
finally:
    sqlite3.sqlite3_shutdown()

print(return_value)
 
</code>
One way to fix it at the moment is to make <code>
