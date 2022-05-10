import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE() object.

# The function pointer is called with one integer argument, and
# returns an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The prototype of the function is:
# int callback(int (*func)(int), int arg)

lib.callback.argtypes = (CALLBACK, ctypes.c_int)
lib.callback.restype = ctypes.c_int

# The function to be passed as argument to lib.callback():

@CALLBACK
def my_callback(i):
    print("my_callback", i)
    return i * 2

# Call lib.callback() with my_callback as argument

print(lib.callback(my_callback, 1))

# The following is a function that takes
