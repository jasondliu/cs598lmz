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

class T(threading.Thread):
    def run(self):
        ctypes.pythonapi.Py_AddPendingCall(ctypes.pythonapi.Py_MakePendingCall,
                                           ctypes.cast(my_cb, ctypes.c_void_p))


if __name__ == "__main__":
    t = T()
    t.start()

    t.join()

    print(my_threading_local.a.execute("SELECT test(?, ?)", (1, 2)).fetchone()[0])
</code>

