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

def main():
    sqlite3.sqlite3_initialize()
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.get_ident()), ctypes.py_object(SystemExit))
    sqlite3.sqlite3_open_v2(":memory:", ctypes.pointer(ctypes.c_void(0)), 0x1, None, ctypes.addressof(my_cb))
    sqlite3.sqlite3_shutdown()

main()
</code>

