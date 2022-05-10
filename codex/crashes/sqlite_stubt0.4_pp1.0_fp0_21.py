import ctypes.util
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_load_extension(None, "./test.so", 0, None)
