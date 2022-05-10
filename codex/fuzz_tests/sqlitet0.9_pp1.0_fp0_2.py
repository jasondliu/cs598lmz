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

init_buffer = ctypes.create_string_buffer(b'\x30\x18')
init_buffer2 = ctypes.create_string_buffer(b'\x3A\x14\x30\x18')

sqlite3_add_application_init = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(('sqlite3_add_application_init', ctypes.util.find_library('sqlite3')))
sqlite3_add_application_init(my_cb, 0)

print(my_threading_local.a.execute("select * from test(1, test(2, 3))").fetchall())
print(my_threading_local.a.execute("select * from test(?,?)", [init_buffer, init_buffer2]).fetchall())  # segfault (but should not in 3.7.13)
