import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

# this is the prototype of the function we call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# this is the function we call
restype = ctypes.c_int
argtypes = (prototype, ctypes.c_int)
func = lib.call_function
func.restype = restype
func.argtypes = argtypes

# this is the function pointer argument
def funcptr(n):
    print("funcptr called with", n)
    return n + 1

# this is the argument to the function pointer argument
arg = 3

# call the function
res = func(funcptr, arg)
print("func returned", res)

# call a function with a function pointer argument
# the function pointer argument is a ctypes callback

# this is the prototype of the function we call
prototype = c
