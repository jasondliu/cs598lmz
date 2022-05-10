import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with a URI.

URI = """\
file:test?mode=memory&cache=shared
"""

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

def test(init_callback=None, set_callback=None):
    lib.sqlite3_enable_shared_cache(1)

    lib.sqlite3_initialize()
    if init_callback:
        init_callback()

    db_ptr = ctypes.c_void_p()
    file_ptr = ctypes.c_void_p()

    r = lib.sqlite3_open_v2(
        URI.encode('utf-8'), ctypes.byref(db_ptr),
        ctypes.c_int(1 | 2), None)

    if r:
        raise Exception(lib.sqlite3_errmsg(db_ptr))

    lib.sqlite3_file_control(db_ptr, b'shared-cache', 7, ctypes.byref(file_ptr))

    if set_callback:
        set_
