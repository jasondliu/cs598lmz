import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test default argument handling
#

# Default argument with int
lib.my_function.argtypes = (ctypes.c_int,)
lib.my_function.restype = ctypes.c_int

if lib.my_function() != 42:
    raise RuntimeError("default argument failed 1")

if lib.my_function(24) != 24:
    raise RuntimeError("default argument failed 2")

# Default argument with float
lib.my_function_float.argtypes = (ctypes.c_float,)
lib.my_function_float.restype = ctypes.c_float

if lib.my_function_float() != 3.14:
    raise RuntimeError("default argument failed 3")

if lib.my_function_float(2.72) != 2.72:
    raise RuntimeError("default argument failed 4")

# Default argument with double
lib.my_function_double.argtypes = (ctypes.c_
