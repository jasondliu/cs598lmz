import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a simple argument
# and a simple result

# XXX This is not yet supported by ctypes
#func = lib.my_sqrt
#func.restype = ctypes.c_double
#func.argtypes = ctypes.c_double,

#print func(2.0)

# call a function with a simple argument
# and a simple result
func = lib.my_sqrt
func.restype = ctypes.c_double
func.argtypes = ctypes.c_double,

print func(2.0)

# call a function with a simple argument
# and a simple result
func = lib.my_sqrt
func.restype = ctypes.c_double
func.argtypes = ctypes.c_double,

print func(2.0)

# call a function with a simple argument
# and a simple result
func = lib.my_sqrt
func.restype = ctypes.c
