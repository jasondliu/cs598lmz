import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test a function with a simple argument and return type.
#

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

paramflags = (1, "x")

def func(*args):
    return args[0] * 2

CMPFUNC = prototype(("cmp_func", lib), paramflags)

result = CMPFUNC(6)
if result != 12:
    raise RuntimeError("CFUNCTYPE for c_int failed")

#
# Test a function with a simple argument and return type,
# using a callable instead of a C function name.
#

CMPFUNC = prototype(("cmp_func", lib), paramflags)

result = CMPFUNC(6)
if result != 12:
    raise RuntimeError("CFUNCTYPE for c_int failed")

#
# Test a function with a simple argument and return type,
# using
