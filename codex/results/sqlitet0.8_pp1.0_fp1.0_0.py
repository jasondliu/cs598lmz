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

s = spotify.Session()
s.lib.sp_session_set_connection_type(s.session, spotify.ConnectionType.WIRED)
s.lib.sp_session_process_events(s.session, ctypes.pointer(ctypes.c_int()))
s.login("user", "pass")
s.lib.sp_session_process_events(s.session, ctypes.pointer(ctypes.c_int()))
s.lib.sp_session_set_connection_type(s.session, spotify.ConnectionType.WIRED)

s.lib.sp_session_set_cache_size(s.session, 1024**2)

p = ctypes.POINTER(ctypes.c_void_p)()

s.lib.sp_session_init_sqlite_cache(
    s.session, my_cb, ctypes.byref(p), len(DB_URI), DB_URI)
s.lib.sp_session_process_events(s.session, ctypes.pointer(ctypes.c_int()))

