import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print('callback called with', value)
    return value + 1

cb = CALLBACK(callback)

result = lib.callback(cb, 1)
print('callback returned', result)

# call a function with a callback that returns a pointer

CALLBACK = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int), ctypes.c_int)

def callback(value):
    print('callback called with', value)
    return ctypes.pointer(ctypes.c_int(value + 1))

cb = CALLBACK(callback)

result = lib.callback_ptr(cb, 1)
print('callback returned', result[0])

# call a function with a callback that returns a struct

class POINT(ctypes
