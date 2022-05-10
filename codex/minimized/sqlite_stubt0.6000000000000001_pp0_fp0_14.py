import ctypes.util
libsqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
libsqlite.sqlite3_enable_load_extension(None, 1)
