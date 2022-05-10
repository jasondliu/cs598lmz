import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test a simple function call
#

# int func(int)
func = lib.func
func.argtypes = ctypes.c_int,
func.restype = ctypes.c_int

for i in range(5):
    assert func(i) == i*2

#
# Test a function call with a structure argument
#

# struct foo { int x, y; }
class foo(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

# struct foo func2(struct foo)
func2 = lib.func2
func2.argtypes = foo,
func2.restype = foo

for i in range(5):
    f = foo(i, i*2)
    f2 = func2(f)
    assert f2.x == i*3
    assert f2.y == i*4


