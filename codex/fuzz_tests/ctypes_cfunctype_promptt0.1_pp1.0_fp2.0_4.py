import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the signature:
# int func(double)
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

# This is the function to pass to the dll.
def callbackfunc(value):
    print('callbackfunc called with', value)
    return 42

# Call the dll function, passing callbackfunc as the argument
lib.set_callback(CALLBACKFUNC(callbackfunc))

# Call the dll function, which will call the callback function
lib.call_callback(3.14)

# This is a function that takes a function pointer as argument.
# The function pointer must have the signature:
# int func(double)
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

# This is the function to pass to the
