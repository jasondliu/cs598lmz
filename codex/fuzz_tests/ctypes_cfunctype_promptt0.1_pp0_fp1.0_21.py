import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test a simple function call
#

# This is the prototype of the function we'd like to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we'd like to call
paramflags = (1, "x"),
restype = ctypes.c_int

# This is the function we'd like to call
func = prototype((restype, paramflags),
                 (lib, "_testfunc_i_i"))

# This is the function we'd like to call
func.errcheck = ctypes.check_error(restype, paramflags)

# This is the function we'd like to call
func.__doc__ = "int testfunc(int x)"

# This is the function we'd like to call
func.__name__ = "testfunc"

# This is the function we'd like to call
func.__module__ = "ctypes_test"

