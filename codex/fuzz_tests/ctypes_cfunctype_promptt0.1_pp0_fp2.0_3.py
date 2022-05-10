import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE() object.

# The function is called with an integer argument, and returns
# the square of this argument.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print('callback called with value:', value)
    return value * value

# The callback is called by the following function:

lib.set_callback.argtypes = (CALLBACK,)
lib.set_callback.restype = None

lib.set_callback(CALLBACK(callback))

# Now call the function that calls the callback:

lib.call_callback.argtypes = (ctypes.c_int,)
lib.call_callback.restype = ctypes.c_int

result = lib.call_callback(5)
print('
