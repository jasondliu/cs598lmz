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
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    c_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    sqlite3.enable_callback_tracebacks(True)
    conn.enable_load_extension(True)
    result = sqlite3.RegisterExtension("test", c_cb)
    assert result == 0
    result = conn.execute("select load_extension('test');")

    try:
        conn.execute('select test(1,2)')
    except sqlite3.DatabaseError as e:
        if e.__class__.__name__ == "DatabaseError":
            print(e.message)

        if e.__class__.__name__ == "DatabaseError":
            print(e.message)

        if e.__class__.__name__ == "DatabaseError":
            print(e.message)

