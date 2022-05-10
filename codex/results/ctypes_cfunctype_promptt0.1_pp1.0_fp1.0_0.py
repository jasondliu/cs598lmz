import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a simple prototype
func = lib.my_function
func.argtypes = None, ctypes.c_int
func.restype = ctypes.c_int

print func(42)

# call a function with a more complex prototype
func = lib.my_other_function
func.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_int
func.restype = ctypes.c_int

print func(1, 2, 3)

# call a function with a function pointer as argument
func = lib.my_callback_function
func.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int
func.restype = ctypes.c_int

def callback(value):
    print "callback called with value", value
    return value + 1

print func(callback, 42)

# call a function
