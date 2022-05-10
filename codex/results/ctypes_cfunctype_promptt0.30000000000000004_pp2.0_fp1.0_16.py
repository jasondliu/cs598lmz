import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a CFUNCTYPE argument

# This is the prototype of the function we call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we call
func = lib.callback
func.argtypes = (prototype, ctypes.c_int)
func.restype = ctypes.c_int

# This is the function we pass as argument
@prototype
def callback(i):
    return i * 2

print(func(callback, 5))

# call a function with a CFUNCTYPE argument, and a pointer to the
# function as well

# This is the prototype of the function we call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we call
func = lib.callback_ptr
func.argtypes = (prototype, ctypes.POINTER(prototype),
