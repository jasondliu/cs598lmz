import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_double)
def test_cf_double():
    return 0.0

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def test_cf_int_int(x):
    return x * 2

@ctypes.CFUNCTYPE(None)
def test_cf_void():
    return

@ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
def test_cf_double_double_double(x, y, z):
    return x + y + z

@ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
def test_cf_double_double_double_double(x, y, z, w):
    return x + y + z + w

# Test ctypes.WINFUNCTYPE
@ctypes.WINFUNCTYPE(
