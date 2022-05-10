import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is a function pointer
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

# This is a function
def func(arg):
    return arg + 1

# This is a function pointer
fptr = prototype(func)

# This is a function pointer
fptr2 = prototype(lambda arg: arg + 1)

# This is a function pointer
fptr3 = prototype(lambda arg: arg + 1)

# This is a function pointer
fptr4 = prototype(lambda arg: arg + 1)

# This is a function pointer
fptr5 = prototype(lambda arg: arg + 1)

# This is a function pointer
fptr6 = prototype(lambda arg: arg + 1)

# This is a function pointer
fptr7 = prototype(lambda arg:
