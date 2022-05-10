import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    # Test CFUNCTYPE(None)
    c_func = ctypes.CFUNCTYPE(None)(lambda: None)
    assert c_func() is None
    # Test CFUNCTYPE(int)
    c_func = ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 42)
    assert c_func() == 42
    # Test CFUNCTYPE(int, int)
    c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 42)
    assert c_func(0) == 42
    assert c_func(1) == 43
    # Test CFUNCTYPE(int, int, int)
    c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(
        lambda x, y: x + y)
    assert c_func(0, 0) == 0
    assert c_func(0
