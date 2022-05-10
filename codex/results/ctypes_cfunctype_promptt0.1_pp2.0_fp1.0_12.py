import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a pointer argument
#
# prototype:
#   int func(int *p)
#
# call:
#   func(&i)

func = lib.func
func.restype = ctypes.c_int
func.argtypes = (ctypes.POINTER(ctypes.c_int),)

i = ctypes.c_int(42)
func(i)
print(i.value)

# call a function with a pointer argument
#
# prototype:
#   int func(int *p)
#
# call:
#   func(i)

func = lib.func
func.restype = ctypes.c_int
func.argtypes = (ctypes.c_int,)

i = ctypes.c_int(42)
func(i)
print(i.value)

# call a function with a pointer argument
#
# prototype:
#   int func(int *p)

