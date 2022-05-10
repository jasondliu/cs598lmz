import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function with a callback
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define a callback function
@prototype
def callback(i):
    print("callback", i)
    return i + 1

# call a function that takes a callback
lib.pass_in_a_callback(callback)

# pass a callback to a function that returns a callback
cb = lib.return_a_callback(callback)
print(cb(1))

# pass a callback to a function that returns a callback
# and call the returned callback
cb = lib.return_a_callback(callback)
print(cb(1))

# pass a callback to a function that returns a callback
# and call the returned callback
cb = lib.return_a_callback(callback)
print(cb(1))

# pass a callback to a function that returns a callback
# and call the returned callback
cb = lib.return_
