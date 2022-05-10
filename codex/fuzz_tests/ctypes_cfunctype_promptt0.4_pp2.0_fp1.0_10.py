import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function with a callback
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define a callback function
@prototype
def callback(i):
    print 'called back with', i
    return i * 2

# call a C function that takes the callback
result = lib.callback(callback, 1)
print result

if result != 2:
    raise RuntimeError("callback() returned wrong value")
