import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test a simple function call
#

# This is the prototype of the function we'd like to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Here's the function
restype = ctypes.c_int
argtypes = (ctypes.c_int,)
func = prototype((restype, argtypes),
                 (lib._testfunc_i_i, "testfunc_i_i"))

# Call the function
res = func(42)
if res != 42:
    raise RuntimeError("function call failed")

#
# Test a function call with a structure as argument and result
#

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

# This is the prototype of the function we'd like to call
prototype = ctypes.CFUNCTYPE(Point
