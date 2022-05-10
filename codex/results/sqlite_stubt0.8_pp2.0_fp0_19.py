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

    return 1;

# Below is a workaround for a bug in iOS, but it makes Android
# crash in a segfault. So only use it in iOS.
if platform.machine()[:3] == 'arm':
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.bind_textdomain_codeset.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    libc.bind_textdomain_codeset('Python', 'UTF-8')

sqlite3.enable_callback_tracebacks(True)
sqlite3.sqlite3_open_v2(DB_URI, ctypes.pointer(ctypes.c_void_p()), 0x100, None)
sqlite3.sqlite3_progress_handler(my_threading_local.a.db, 1, my_cb, None);
sqlite3.sqlite3_close(my_threading_local.a.db);
