import ctypes
# Test ctypes.CFUNCTYPE


def test_CFUNCTYPE():
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    assert f(1, 2) == 0
    assert f.restype == ctypes.c_int
    assert f.argtypes == [ctypes.c_int, ctypes.c_int]
