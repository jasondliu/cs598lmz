import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that we pass to the dll.

def callback(n):
    print("callback called with", n)
    return n + 1

# This is the function in the dll that takes the function pointer.

lib.set_callback.argtypes = CALLBACKFUNC,
lib.set_callback.restype = None

# Now set the callback in the dll

lib.set_callback(CALLBACKFUNC(callback))

# Now call the function in the dll that will call our callback.

lib.call_callback(3)

# Now test that the callback is still set.

lib.call_callback(4)

# Now test that we
