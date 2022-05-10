import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

def func(*args):
    print("func", args)
    return args[-1]

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

res = lib.callback(CALLBACK(func), 1, 2)
if res != 2:
    raise Exception("Wrong result")

# call a function with a function pointer argument
# the function pointer argument is a ctypes callback instance

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(lambda x, y: x + y)
res = lib.callback(callback, 1, 2)
if res != 3:
    raise Exception("Wrong result")

# call a function with a function pointer argument
