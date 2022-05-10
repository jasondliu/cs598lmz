import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type, it should be callable
# and should have a restype attribute.

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib.myfunc)

print(func(1))
print(func.restype)

# This is a pointer to a function pointer type, it should
# be callable and should have a restype attribute.

func = ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))(lib.myfunc)

print(func(1))
print(func.restype)

# This is a pointer to a function pointer type, it should
# be callable and should have a restype attribute.

func = ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))(lib.myfunc)

print(func
