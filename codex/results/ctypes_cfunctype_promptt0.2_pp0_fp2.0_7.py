import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this is a function that takes a function pointer as an argument
# and calls it.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with argument", arg)
    return arg + 1

# call the function with a ctypes callback
i = CALLBACKFUNC(callback)
lib.pass_func(i)

# call the function with a python callback
lib.pass_func(callback)

# call a function with a function pointer result
# this is a function that returns a function pointer

def my_callback(arg):
    print("my_callback called with argument", arg)
    return arg + 1

# call the function with a ctypes callback
i = CALLBACKFUNC(my_callback)
lib.return_func(i)

# call the function with a python callback

