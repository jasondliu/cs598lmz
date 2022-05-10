import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A function with a double argument, returning a double
func = ctypes.CFUNCTYPE(ctypes.c_double)(("testfunc", lib), ((1, "x"),))

print func(0.0)
print func(1.0)
print func(2.0)
print func(3.0)

# A function with an int argument, returning a pointer to int
func = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int))(("testfunc_p", lib), ((1, "x"),))

print func(0)
print func(1)
print func(2)
print func(3)

# A function with a void argument, returning void
func = ctypes.CFUNCTYPE(None)(("testfunc_v", lib), ((1, "x"),))

func()

# A function with a double argument, returning a double
func = ctypes.CFUNCTYPE
