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

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_open(":memory:", ctypes.byref(my_threading_local.db))
sqlite3.sqlite3_create_module_v2(
    my_threading_local.db,
    b"test",
    ctypes.cast(0, ctypes.c_void_p),
    0,
    my_cb
)
sqlite3.sqlite3_close(my_threading_local.db)
sqlite3.sqlite3_shutdown()
</code>
I'm using Python 3.6.7.  I'm also using SQLite 3.27.2.  I'm using Ubuntu 18.04.2 LTS.  I'm using the latest version of ctypes.  I'm using:
<code>$ gcc --version
gcc (Ubuntu 7.3.0-27ubuntu1~18.04) 7.3.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is
