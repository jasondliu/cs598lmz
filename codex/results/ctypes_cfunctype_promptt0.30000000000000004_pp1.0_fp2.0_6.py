import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int)]

def func(a, b, c):
    return a.a + b.b + c.c

CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, X, Y, Z)

f = CFuncPtr(func)

x = X(1)
y = Y(2)
z = Z(3)

print f(x, y, z)

if ctypes.sizeof(CFuncPtr) != ctypes.sizeof(ctypes.c_void_p):
    raise Exception("sizeof(CFUNCTYPE) != sizeof(void *)")

# Test ctypes.WINFUNCTYPE
import _ctypes_test
