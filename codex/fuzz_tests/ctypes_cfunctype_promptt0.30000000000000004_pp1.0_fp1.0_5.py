import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# First try a simple function
#

func = lib.my_function
func.argtypes = (ctypes.c_int, ctypes.c_int)
func.restype = ctypes.c_int

print func(1, 2)

#
# Now try a function pointer
#

func = lib.my_function_pointer
func.argtypes = (ctypes.c_int, ctypes.c_int)
func.restype = ctypes.c_int

print func(1, 2)

#
# Now try a function pointer in a structure
#

class X(ctypes.Structure):
    _fields_ = [("func", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int))]

x = X()
x.func = func

print x.func(1, 2)

#
# Now try a function pointer
