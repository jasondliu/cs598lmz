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

# Call the dll function.

lib.set_callback(CALLBACKFUNC(callback))

# Call the function pointer in the dll.

lib.call_callback(1)

# Call the function pointer in the dll again.

lib.call_callback(2)

# Call the function pointer in the dll again.

lib.call_callback(3)

# Call the function pointer in the dll again.

lib.call_callback(4)

# Call the function pointer in the dll again.
