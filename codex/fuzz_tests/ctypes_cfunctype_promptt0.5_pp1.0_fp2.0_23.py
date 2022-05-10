import ctypes
# Test ctypes.CFUNCTYPE

def test_CFUNCTYPE():
    from ctypes import c_int
    from ctypes import CFUNCTYPE

    f = CFUNCTYPE(c_int, c_int)
    assert f(1) == 1
    f = CFUNCTYPE(c_int, c_int, c_int)
    assert f(1, 2) == 1
    f = CFUNCTYPE(c_int, c_int, c_int, c_int)
    assert f(1, 2, 3) == 1
    f = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int)
    assert f(1, 2, 3, 4) == 1
    f = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int, c_int)
    assert f(1, 2, 3, 4, 5) == 1
    f = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int
