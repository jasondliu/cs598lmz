import ctypes
# Test ctypes.CFUNCTYPE
def f(x):
    return x + 1
F = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(f)
assert F(1) == 2
# Test ctypes.PYFUNCTYPE
def f(x):
    return x + 1
F = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)(f)
assert F(1) == 2
# Test ctypes.WINFUNCTYPE
def f(x):
    return x + 1
try:
    _ = ctypes.WINFUNCTYPE
except AttributeError:
    pass
else:
    F = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)(f)
    assert F(1) == 2

# Test ctypes.addressof
import ctypes
a = ctypes.c_int()
b = ctypes.c_int()
addr_a = ctypes.addressof(a)
