import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as an argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 1

# This is the function that calls the callback function
lib.call_callback.argtypes = (CALLBACK, ctypes.c_int)
lib.call_callback.restype = ctypes.c_int

# Call the function
res = lib.call_callback(CALLBACK(callback), 1)
print("result:", res)

# Call the function again, this time with a different callback
def callback2(arg):
    print("callback2 called with", arg)
    return arg + 2

res = lib.call_callback(CALLBACK(callback2), 1)
print("result:", res)

# Call the function again, this time
