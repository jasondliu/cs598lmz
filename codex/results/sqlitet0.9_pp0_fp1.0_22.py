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

if __name__ == "__main__":
    sqlite3.enable_callback_tracebacks(True)
    dll = DB_URI.startswith("file:") and ctypes.util.find_library(
        "sqlite3"
    ) or None
    db = sqlite3.connect(DB_URI, uri=True)
    ctypes.pythonapi.PyEval_SetProfile(my_cb, id(my_cb))
    db.execute("select test(test(test(test(test(test('test'))))))")
    """
#0  0x00007ffff64f829e in ?? () from /Users/me/src/pysqlite/test/sqlite3.so
#1  0x00007ffff64ed187 in test_fn (a=...) at test_support.pyx:148
#2  0x0000000100001cc8 in op_Function ()
#3  0x0000000100006c8c in sqlite3VdbeExec ()
#4  0x0000000100005d45 in sqlite3
