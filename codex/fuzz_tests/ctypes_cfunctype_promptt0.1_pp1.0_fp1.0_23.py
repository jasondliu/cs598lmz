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

# This is the function in the dll that takes the function pointer.

lib.set_callback.argtypes = CALLBACKFUNC,
lib.set_callback.restype = None

# Now we can call the function in the dll.

lib.set_callback(CALLBACKFUNC(callback))

# And this calls the function pointer.

lib.call_callback(5)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# a pointer to a character.
