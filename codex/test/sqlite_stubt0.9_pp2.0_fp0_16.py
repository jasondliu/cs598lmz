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

p = ctypes.pointer(ctypes.c_int(5))

sqlite3.enable_callback_tracebacks(True)

try:
    sqlite3.set_authorizer(my_cb)
except Exception:
    pass

sqlite3.enable_shared_cache(True)

if hasattr(sqlite3, 'enable_load_extension'):
    sqlite3.enable_load_extension(True)
    d = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    d.execute("select load_extension('xxx')") # file doesn't exist
    d.close()

@ignore_exceptions
def test_main(extension_loader):
    if extension_loader:
        extmod = extension_loader.sqlite_test_extension_load()
    else:
        extmod = None

    # warning: extension functions are not deleted properly !
    if extmod:
        extmod.delete_custom_functions()

