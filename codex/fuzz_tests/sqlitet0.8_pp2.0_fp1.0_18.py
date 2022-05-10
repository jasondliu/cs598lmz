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

if __name__ == '__main__':
    sqlite3._sqlite.sqlite3_threadsafe()

    my_p = ctypes.pointer(ctypes.c_int())
    sqlite3.register_converter("test", my_cb)
    conn = sqlite3.connect(DB_URI, uri=True)

    cursor = conn.cursor()
    cursor.execute("select 1")
    cursor.execute("select cast(? as test)", ("a",))

    my = my_threading_local.a

    cursor.execute("select 1")
    cursor.execute("select test(1, ?)", (1,))

    del cursor
    conn.close()

    print("Ending of python script")
</code>

Deleting/closing the cursor seems to close the connection of the first thread.  
Is there a way to keep the connection alive?
Is there a way to fix this issue? Or do I need to do something different?
Or do I need to use the multi-threaded mode?



A:

I am dealing
