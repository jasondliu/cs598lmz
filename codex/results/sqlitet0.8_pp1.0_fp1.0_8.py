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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_config(0x00070000, 0)

lib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p(0)), 0x00000400, None)

lib.sqlite3_enable_load_extension(0, 1)

lib.sqlite3_load_extension("sqlite3_python.so", None, ctypes.cast(my_cb, ctypes.c_void_p))

conn_a = sqlite3.connect(DB_URI, uri=True)

cursor_a = conn_a.cursor()

cursor_a.execute("create table foo (a); insert into foo values(test(2, 3));")
cursor_a.execute("select * from foo")

print(cursor_a.fetchall())

conn_a.close()

lib.sqlite3_close(
