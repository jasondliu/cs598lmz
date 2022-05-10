import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a simple prototype
func = lib.my_function
func.argtypes = None, ctypes.c_int
func.restype = ctypes.c_int

print func(42)

# call a function with a more complicated prototype
func = lib.my_other_function
func.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_int
func.restype = ctypes.c_int

print func(1, 2, 3)

# call a function with a prototype that uses a pointer
func = lib.my_third_function
func.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_int)
func.restype = ctypes.c_int

i = ctypes.c_int(42)
print func(1, ctypes.byref(i))
print i.value

# call a function with a prototype that uses a pointer to
