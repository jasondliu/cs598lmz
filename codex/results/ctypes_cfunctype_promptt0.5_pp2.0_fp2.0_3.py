import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    # test return values
    f1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
    assert f1(42) == 42
    f2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
    assert f2(41) == 42
    f3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x * 2)
    assert f3(21) == 42
    # test simple args
    f4 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
    assert f4(42) == 42
    f5 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
    assert f5(41) == 42
    f6 = ctypes.CFUNCTY
