import ctypes
# Test ctypes.CFUNCTYPE

# This test is not complete, but it does test some of the more
# interesting aspects of ctypes.CFUNCTYPE.

from ctypes import *
import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# This function is called from C, and returns a pointer to a function
# pointer.

get_func = lib.get_func
get_func.restype = c_void_p

# This function is called from C, and expects a pointer to a function
# pointer as argument.

call_func = lib.call_func
call_func.argtypes = c_void_p,

# This function is called from C, and expects a pointer to a function
# pointer as argument.  It calls the function pointer, and returns
# the result.

call_func_result = lib.call_func_result
call_func_result.argtypes = c_void_p,
call_func_result.restype = c_int

# This function is called from C, and expects a pointer to a function
# pointer
