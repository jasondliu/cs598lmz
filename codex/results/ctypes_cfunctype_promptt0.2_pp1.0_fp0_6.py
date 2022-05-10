import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function with a callback argument.
# The callback is called with a pointer to an int.
# The callback returns an int.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def func(n):
    print('func', n)
    return n * 2

callback = prototype(func)

# Call the function with the callback.

res = lib.use_callback(callback)
print(res)

# Call the function with a callback that raises an exception.

def func(n):
    print('func', n)
    raise ValueError

callback = prototype(func)

try:
    res = lib.use_callback(callback)
except ValueError:
    print('ValueError')

# Call the function with a callback that returns a value that doesn't fit
# in an int.

def func(n):
    print('func',
