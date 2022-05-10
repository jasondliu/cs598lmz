import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This one is a function that takes a function pointer as argument
# and calls the function.
func = lib.pass_func
func.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
func.restype = ctypes.c_int

# The function to be passed as argument
def funcptr(value):
    print('funcptr called with', value)
    return value + 1

# Call the function
print(func(funcptr))

# This one is a function that returns a function pointer
func = lib.return_func
func.restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Call the function
f = func()
print(f(42))

# Test with a prototype
func = lib.return_func
func.restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c
