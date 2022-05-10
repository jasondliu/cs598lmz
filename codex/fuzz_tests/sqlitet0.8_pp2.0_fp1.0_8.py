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
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    global DB_URI
    lib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.c_void_p(0x0), 1)

    lib.sqlite3_enable_load_extension(my_threading_local.a.connection, 1)
    lib.sqlite3_load_extension(my_threading_local.a.connection, b"./extension.so", None, None)

    t = threading.Thread(target=main)
    t.start()
    t.join()

    # after the t.join, accessing the conn object in my_threading_local segfaults
    with my_threading_local.a:
        print()

main()
```

I looked into this problem a bit more, and it seems that there may be some weirdness with the way sqlite is loaded. `sqlite3_open_v2` is called, which spawns a new
