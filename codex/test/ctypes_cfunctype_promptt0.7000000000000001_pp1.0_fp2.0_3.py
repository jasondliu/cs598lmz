import ctypes
# Test ctypes.CFUNCTYPE()
# This tests that the C compiler supports the C99 'restrict' keyword.
def test_cfunctype():
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_float)

