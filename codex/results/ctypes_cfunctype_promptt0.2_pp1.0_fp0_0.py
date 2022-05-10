import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we want to pass to the dll:
def callback(number):
    print('callback called with', number)
    return number + 42

# Now we can pass our callback to the dll:
lib.set_callback(CALLBACKFUNC(callback))

# And call the dll function that calls our callback:
lib.call_callback(5)

# The callback should have been called with 5, and the dll
# should have returned 47.

if lib.call_callback(5) != 47:
    raise Exception("callback wasn't called")

# Now we can pass our callback to the dll:
lib.set_callback(CALLBACKFUNC(callback
