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

async def async_fn():
    await aio.sleep(1)

def main():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_ASYNC, 1)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)
    sqlite3.sqlite3_enable_shared_cache(1)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_load_extension(sqlite3.sqlite_handle(0), 1)
    lib.sqlite3_load_extension(sqlite3.sqlite_handle(0), str(Path(".").absolute() / "extension" / "sqlite3_extension.so"), None, ctypes.cast(None, ctypes.c_void_p))


