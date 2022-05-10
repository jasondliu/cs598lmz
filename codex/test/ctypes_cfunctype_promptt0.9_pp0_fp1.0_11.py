import ctypes
# Test ctypes.CFUNCTYPE
def test_global_func(value):
    return value * 3
ctypes.CFUNCTYPE(ctypes.c_int)(test_global_func)(2)

# Test ctypes.WINFUNCTYPE
def test_win_func(value):
    return value * 4
