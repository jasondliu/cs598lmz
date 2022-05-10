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
    sqlite3.enable_load_extension(True)
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(ctypes.c_int(3), ctypes.c_int(1))
    lib.sqlite3_initialize()

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    lib.sqlite3_auto_extension(f)

    x = conn.execute("SELECT load_extension('test')")
    print(x.fetchall())

    with conn:
        conn.execute("CREATE TABLE test (id INTEGER)")
        conn.execute("INSERT INTO test VALUES (test(1, 2))")

    x = my_threading_local.a
    x.execute('SELECT * FROM test')
    print
