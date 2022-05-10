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

def call_w_uri():
    p = sqlite3.backup_init(my_threading_local.a, 'main', my_threading_local.a, 'main')
    sqlite3.backup_step(p, 1)
    sqlite3.backup_finish(p)

sqlite3.sqlite3_open_v2(
    ctypes.POINTER(sqlite3.sqlite3)(),
    DB_URI,
    ctypes.c_void_p(-1),
    ctypes.c_char_p(":memory:"),
    0,
    ctypes.c_char_p("")
)

module = sqlite3.load_extension("sqlite3-regexp")

# call_w_uri raises:
# segfault: libc.so.6()(+0x121309)[0x7f9d20f35309]
# raise_exception() at src/thread/mod.rs:197
# std::sys_common::backtrace::_print() at
