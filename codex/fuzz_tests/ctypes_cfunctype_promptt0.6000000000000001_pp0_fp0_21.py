import ctypes
# Test ctypes.CFUNCTYPE
def foo(x, c):
    c.value = c.value * 2
    return x * 2

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))(foo)
c = ctypes.c_int(12)
assert cb(3, c) == 6
assert c.value == 24

# Test ctypes.PYFUNCTYPE
def pyfoo(x, c):
    c.value = c.value * 2
    return x * 2

cb = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))(pyfoo)
c = ctypes.c_int(12)
assert cb(3, c) == 6
assert c.value == 24

# Test ctypes.WINFUNCTYPE
def winfoo(x, c):
    c.value = c.value * 2
    return x * 2

cb = c
