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

sqlite3.enable_callback_tracebacks(True)
assert sqlite3.enable_callback_tracebacks()

sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), ctypes.c_int(1))
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_LOG), my_cb)

print(sqlite3.threadsafety)
print(sqlite3.sqlite_version)
print(sqlite3.sqlite_version_info)
print(sqlite3.sqlite_source_id)
print(sqlite3.sqlite_compiletime_options)
print(sqlite3.sqlite_compile_options)
print(sqlite3.PARSE_DECLTYPES)
print(sqlite3.PARSE_COLNAMES)
print(sqlite3.complete_statement("SELECT 1;"))
print(sqlite3.complete_statement("SELECT 1;"))
print(sqlite3.complete_statement("
