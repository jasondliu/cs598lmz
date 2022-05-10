import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to call.  It takes a function pointer as
# argument.

lib.pass_int_callback.argtypes = (CALLBACK,)
lib.pass_int_callback.restype = ctypes.c_int

# This is the function to pass as argument.

def callback(value):
    print('callback called with value %d' % value)
    return value + 1

# Call the function with the function pointer

result = lib.pass_int_callback(CALLBACK(callback))
print('result =', result)

# This is a function that takes a function pointer as argument.
# The function pointer must have no arguments, and returns
# an integer.


