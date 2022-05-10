import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that we pass to the dll.

def callback(i):
    print("callback", i)
    return i + 1

# Call the dll function, passing callback.

lib.set_callback(CALLBACKFUNC(callback))

# Now call the dll function that calls our callback.

lib.call_callback(5)

# The callback should have been called with argument 5, and
# the return value should be 6.

print("DONE")
