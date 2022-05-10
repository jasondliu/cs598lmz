import ctypes
# Test ctypes.CField, ctypes.Field, ctypes.Array.
import _ctypes_test

lib = _ctypes_test.lib

# Test the return type attribute of functions.
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

lib.returns_X.restype = X
Xp = ctypes.POINTER(X)
lib.returns_X.restype = Xp

lib.returns_X.restype = ctypes.c_int

lib.returns_X.restype = Y
lib.returns_X.restype = Yp = ctypes.POINTER(Y)

def test():
    lib.returns_X.restype = Z

try:
    test()
except ValueError, details:
    if details.args[0]
