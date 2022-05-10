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

hashtable = ctypes.c_byte * 32
hashtable = ctypes.cast(hashtable(), ctypes.POINTER(ctypes.c_byte))

some_uri = 'file:master?mode=memory'

a = sqlite3.connect(some_uri, uri=True)
a.enable_shared_cache(True)

thread = threading.Thread(target=my_cb, args=(hashtable, ))
thread.start()
thread.join()

#print(my_threading_local.a.execute("INSERT INTO tbl VALUES(test(?, ?), test(?, ?))", (1, 2, 3, 4)).fetchall())
</code>
Every time I execute the code, I get a SegmentationFault when calling test_fn in another thread (see last 4 lines, they should print [(1, 3), (1, 3)]).
Running cProfile with the following shows that there is a segmentation fault during the <code>_sqlite3.connect</code> method on line 804, which is in the <code>__del__
