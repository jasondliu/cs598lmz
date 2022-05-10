import ctypes
# Test ctypes.CFUNCTYPE with nested prototypes
from ctypes import *
import _ctypes_test

prototype = CFUNCTYPE(c_int, c_int, c_int, c_int)
class X(Union):
    _fields_ = [("x", prototype),
                ("y", prototype)]

lib = CDLL(_ctypes_test.__file__)

lib.return_17.restype = c_int
lib.return_17.argtypes = [c_int, c_int]

lib.return_arg.restype = c_int
lib.return_arg.argtypes = [c_int]

x = X.x
y = X.y

test_func = x(lambda a,b,c: lib.return_17(a, b) + lib.return_arg(c))
assert 17 == test_func(1, 2, 3)

test_func = y(lambda a,b,c: lib.return_17(a, b) + lib.return_arg(c))
assert 17 == test_func(1, 2, 3)

