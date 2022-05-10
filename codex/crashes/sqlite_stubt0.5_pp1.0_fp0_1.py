import ctypes.util
def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
def test_functions():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    lib.sqlite3_create_function_v2(ctypes.c_void_p(), b"test", 2, 1, cb, None, None, None)
if __name__ == "__main__":
    test_functions()
