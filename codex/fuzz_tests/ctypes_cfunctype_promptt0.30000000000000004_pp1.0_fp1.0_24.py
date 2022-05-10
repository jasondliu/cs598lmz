import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call_function takes a function pointer and an integer argument.  It
# calls the function with the integer argument and returns the result
call_function = lib.call_function
call_function.restype = ctypes.c_int
call_function.argtypes = (ctypes.c_void_p, ctypes.c_int)

# int_func takes an integer argument and returns it
int_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(
    lambda x: x + 42)

# call int_func through call_function
res = call_function(int_func, 5)
if res != 47:
    raise RuntimeError("CFUNCTYPE test failed")

# int_func2 takes no arguments and returns 42
int_func2 = ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 42)

# call int_func2 through call_function
res = call
