import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The function to be called.
def func(arg):
    print("called with", arg)
    return arg + 1

# Callback function wrapper
callback = CALLBACK(func)

# Call the function that takes a function pointer
lib.pass_func(callback)

# Call the function that takes a function pointer, and pass None
lib.pass_func(None)

# Call the function that takes a function pointer, and pass a
# function that takes more arguments than the callback expects
def func2(arg1, arg2):
    print("called with", arg1, arg2)
    return arg1 + arg2

callback2 = CALLBACK(func2)

lib.pass_func(callback2)

# Call the function that takes a function pointer
