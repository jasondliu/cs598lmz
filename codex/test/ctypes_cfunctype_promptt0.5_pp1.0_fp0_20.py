import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    assert ctypes.CFUNCTYPE(ctypes.c_int) is ctypes.CFUNCTYPE(ctypes.c_int)
    assert ctypes.CFUNCTYPE(ctypes.c_int) is not ctypes.CFUNCTYPE(ctypes.c_short)
    assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int) is ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int) is not ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_short)
    assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int) is ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    assert ctypes.CFUN
