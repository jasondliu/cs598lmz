import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    def func(a, b):
        return a + b
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3
    assert cfunc(1, 2) == 3

