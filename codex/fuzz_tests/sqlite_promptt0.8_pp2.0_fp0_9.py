import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper

def load_library():
    # this is for OS X
    lib_paths = [
        './lib/libsqlite3.so',
        '/opt/local/lib/libsqlite3.dylib',
    ]
    for path in lib_paths:
        try:
            return ctypes.CDLL(path)
        except OSError:
            continue
    raise OSError(
        "Could not find sqlite3 library. "
        "Try setting the LD_LIBRARY_PATH environment variable."
    )

_lib_path = ctypes.util.find_library('sqlite3')
if _lib_path is None:
    _sqlite_lib = load_library()
else:
    _sqlite_lib = ctypes.CDLL(_lib_path)
    
_sqlite_lib.sqlite3
