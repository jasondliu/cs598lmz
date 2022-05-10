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


class MyFunc(ctypes.c_int):
    def __init__(self):
        super(MyFunc, self).__init__(my_cb)


my_func = MyFunc()

atom = ctypes.c_char_p.in_dll(
    ctypes.pythonapi,
    "Py_TextString"
)

def main():
    callback = sqlite3.FFI.CData.from_buffer(
        my_func
    )

    for i in xrange(2):
        db = sqlite3.connect(DB_URI, uri=True)
        db.create_function(
            "my_cb",
            1,
            callback
        )
        cursor = db.cursor()
        cursor.execute("select my_cb(1)")
        a = cursor.fetchone()
        cursor.close()
        db.close()
        assert a == (1,)
        del a
        del cursor
        del db

