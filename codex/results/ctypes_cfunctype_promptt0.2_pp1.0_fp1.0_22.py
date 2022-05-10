import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function with a callback
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# define a callback function
@prototype
def callback(a, b):
    print("callback(%d, %d)" % (a, b))
    return a * b

# register the callback
lib.set_callback(callback)

# call a function that calls the callback
print(lib.call_callback(2, 3))
