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

sqlite3.sqlite3_extension_init(ctypes.c_void_p(), None)
sqlite3.sqlite3_shutdown()

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_initialize()

sqlite3.sqlite3_create_function(None, "test", 1, None, my_cb, None, None, None)

try:
    sqlite3.connect(DB_URI, uri=True)
except sqlite3.DatabaseError:
    pass

sqlite3.sqlite3_shutdown()
</code>
Here is the output of <code>valgrind</code>:
<code>==726== Memcheck, a memory error detector
==726== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==726== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==726== Command: python3 /tmp/
