import ctypes
# Test ctypes.CFUNCTYPE

def test_cfunctype():
    # int (*f)(int)
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)
    assert f(1) == 2
    # int (*f)(int, int)
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(
        lambda x, y: x+y)
    assert f(1, 2) == 3

def test_cfunctype_with_defaults():
    # int (*f)(int, int)
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(
        lambda x, y=2: x+y)
    assert f(1, 2) == 3
    assert f(1) == 3

