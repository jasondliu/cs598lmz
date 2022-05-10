import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a CFUNCTYPE argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@prototype
def func(*args):
    print('func', args)
    return args[0] + 3

result = lib.call_function(func)
if result != 8:
    raise RuntimeError("bad result")

# call a function with a CFUNCTYPE argument, the function takes a pointer
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

@prototype
def func(*args):
    print('func', args)
    v = args[0].contents
    return v.value + 3

result = lib.call_function(func)
if result != 8:
    raise RuntimeError("bad result")

# call a function with a CFUNCTYPE argument, the function takes a
