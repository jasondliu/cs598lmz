import ctypes
# Test ctypes.CFUNCTYPE
def f(a, b):
    return a + b

cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(f)
assert cf(1, 2) == 3
assert cf(3, 4) == 7
# Test ctypes.PYFUNCTYPE
def f(a, b):
    return a + b

pf = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(f)
assert pf(1, 2) == 3
assert pf(3, 4) == 7
# Test ctypes.WINFUNCTYPE
def f(a, b):
    return a + b

