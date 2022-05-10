import ctypes
# Test ctypes.CField.from_param
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Test _CData_from_address()
class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

x = X()
a = ctypes.addressof(x)
assert ctypes.cast(a, ctypes.POINTER(X)).contents.x == 0

# Test _CData_from_address() with an offset
class Y(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", X)]

y = Y()
a = ctypes.addressof(y.y)
assert ctypes.cast(a, ctypes.POINTER(X)).contents.x == 0

# Test _CData_from_address() with a subclass of _CData
class Z(X):
    pass

z = Z()
c = ctypes.cast(ctypes.addressof(z), ctypes.
