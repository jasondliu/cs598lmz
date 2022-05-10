import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callit(func, arg):
    func.argtypes = (ctypes.c_int,)
    func.restype = ctypes.c_int
    return func(arg)

# This is the function passed to the C function.

def func(arg):
    print("func", arg)
    return arg + 1

# This is the function passed to the C function.

def func2(arg):
    print("func2", arg)
    return arg + 2

# Call the C function with func as argument

