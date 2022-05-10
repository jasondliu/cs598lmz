import ctypes
# Test ctypes.CFUNCTYPE
X = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
X.__name__ = 'X'
try:
    X.__qualname__ = 'X'
except AttributeError:
    pass
F = X(lambda x, y: x + y)
assert F(1, 2) == 3
