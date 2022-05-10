import ctypes
# Test ctypes.CFUNCTYPE()
def foo(x, y):
    return x + y

f = ctypes.CFUNCTYPE(ctypes.c_int)(foo)
assert f(1, 2) == 3
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(foo)
assert f(1, 2) == 3

# Test ctypes.WINFUNCTYPE()
def bar(x, y):
    return x + y

f = ctypes.WINFUNCTYPE(ctypes.c_int)(bar)
assert f(1, 2) == 3
f = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(bar)
assert f(1, 2) == 3

# Test ctypes.PYFUNCTYPE()
def baz(x, y):
    return x + y

f = ctypes.PYFUNCTYPE(ctypes.c_int)(baz)
assert f(1,
