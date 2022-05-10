import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 1

cb = CALLBACK(callback)

res = lib.callback(cb, 1)
print("callback returned", res)

# call a function with a callback argument, and pass None

res = lib.callback(None, 1)
print("callback returned", res)

# call a function with a callback argument, and pass a foreign function

res = lib.callback(cb, 1)
print("callback returned", res)

# call a function with a callback argument, and pass a foreign function

res = lib.callback(cb, 1)
print("callback returned", res)

# call a function with a callback argument, and pass a foreign function

res = lib.callback(cb, 1)
print("
