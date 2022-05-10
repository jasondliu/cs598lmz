import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Prototype a function with two int arguments and returning an int
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Create a new function with prototype
restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)
add = prototype((b"add", lib), (restype, argtypes))

# Call the function
print(add(1, 2))

# Prototype a function with no arguments and returning void
prototype = ctypes.CFUNCTYPE(None)

# Create a new function with prototype
restype = None
argtypes = ()
func = prototype((b"func", lib), (restype, argtypes))

# Call the function
func()

# Prototype a function with a double argument and returning a double
prototype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_
