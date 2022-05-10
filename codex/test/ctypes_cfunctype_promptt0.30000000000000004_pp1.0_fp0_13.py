import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b, c):
    return a + b + c

CFUNCTYPE = ctypes.CFUNCTYPE

f = CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

assert f(1, 2, 3) == 6

# Test ctypes.POINTER

POINTER = ctypes.POINTER

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X(42)

px = POINTER(X)(x)
assert px.contents.a == 42

# Test ctypes.byref

byref = ctypes.byref

x.a = 24
