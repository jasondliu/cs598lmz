import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function with a callback
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the callback
@prototype
def callback(i):
    print("callback", i)
    return i + 1

# call the function with the callback
lib.set_callback(callback)

# call the function with the callback
lib.call_callback(1)

# call the function with the callback
lib.call_callback(2)

# call the function with the callback
lib.call_callback(3)

# call the function with the callback
lib.call_callback(4)

# call the function with the callback
lib.call_callback(5)

# call the function with the callback
lib.call_callback(6)

# call the function with the callback
lib.call_callback(7)

# call the function with the callback
lib.call_callback(8)


