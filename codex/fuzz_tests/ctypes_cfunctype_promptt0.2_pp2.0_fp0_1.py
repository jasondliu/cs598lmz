import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a CFUNCTYPE argument

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@prototype
def func(value):
    print("func", value)
    return value + 1

res = lib.call_func(func, 1)
if res != 2:
    raise Exception("wrong result")

# call a function with a CFUNCTYPE argument, and pass a callback

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@prototype
def func(value):
    print("func", value)
    return value + 1

@prototype
def callback(value):
    print("callback", value)
    return value + 1

res = lib.call_func_callback(func, callback, 1)
if res != 3:
    raise Exception("wrong result")

# call a function with a CF
