import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have a simple signature: int()
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int)

@CALLBACK
def callback():
    print("callback() called")
    return 42

lib.set_callback(callback)

lib.call_callback()

# This is a function that takes a function pointer as argument.
# The function pointer must have a simple signature: int()
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@CALLBACK
def callback(arg):
    print("callback() called with", arg)
    return arg + 42

lib.set_callback(callback)

lib.call_callback()

# This is a function that takes a function pointer as argument.
# The function pointer must have a simple signature: int()
CALLBACK = ctypes.
