import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

def callback(x):
    print('callback called with', x)
    return x + 1

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib.set_callback(CALLBACKFUNC(callback))

print(lib.call_callback(5))

# call a function with a callback argument, and pass None

lib.set_callback(CALLBACKFUNC(None))

print(lib.call_callback(5))

# call a function with a callback argument, and pass a function

def callback(x):
    print('callback called with', x)
    return x + 1

lib.set_callback(callback)

print(lib.call_callback(5))

# call a function with a callback argument, and pass a function
# which takes a different number of arguments

def callback():
    print('callback
