import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a callable Python object

def func(*args):
    print(args)
    return args[-1]

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

lib.pass_func(CALLBACK(func), 1, 2, 3)

# call a function with a function pointer argument
# the function pointer argument is a ctypes callback object

@CALLBACK
def func(*args):
    print(args)
    return args[-1]

lib.pass_func(func, 1, 2, 3)

# call a function with a function pointer argument
# the function pointer argument is a ctypes callback object
# created by CFUNCTYPE

lib.pass_func(CALLBACK(func), 1, 2, 3)

# call a function with a function pointer argument
