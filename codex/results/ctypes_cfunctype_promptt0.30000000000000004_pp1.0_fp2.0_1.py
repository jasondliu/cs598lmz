import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Test a function with a simple result
#
restype = ctypes.c_int
res = lib.add_one(1)
assert res == 2

# Test a function with a more complicated result
#
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

restype = X
res = lib.identity(X(1, 2))
assert res.a == 1
assert res.b == 2

# Test a function with a void result
#
restype = None
res = lib.nothing()
assert res is None

# Test a function with a simple argument
#
argtypes = [ctypes.c_int]
res = lib.add_one(1)
assert res == 2

# Test a function with a more complicated argument
#
argtypes = [X]
res = lib.identity(X(1, 2))

