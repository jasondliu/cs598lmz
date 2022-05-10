import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

def func(*args):
    print(args)
    return args[-1]

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

res = lib.use_callback(CALLBACK(func), 1, 2, 3)
if res != 3:
    raise Exception("Bad result: %s" % res)

# call a function with a function pointer argument
# the function pointer argument is a ctypes callback instance

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(lambda x, y: x + y)
res = lib.use_callback(callback, 1, 2)
if res != 3:
    raise Exception("Bad result: %s"
