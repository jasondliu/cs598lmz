import ctypes
ctypes.cast(0, ctypes.py_object);
# sigsys() gets called because libffi calls PyPy_FatalError() when it fails to convert types
dll = CDLL(get_header_dir() + '/../../sqlite3/libsqlite3.so', RTLD_GLOBAL)
dll.sqlite3_open

# __________  Entry point  __________

def target(*args):
    return entry_point, None
