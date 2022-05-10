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

sqlite3.sqlite3_progress_handler(my_cb, 1, ctypes.pointer(ctypes.c_int()))

for i in range(10):
    # This is not really a good test, as the threading local is only
    # deleted at the end of the process (or module, I guess).
    # However, I'm not sure how to get hold of the object without
    # using some form of global variable...
    threading.Thread(target=print, args=(id(my_threading_local.a),)).start()
