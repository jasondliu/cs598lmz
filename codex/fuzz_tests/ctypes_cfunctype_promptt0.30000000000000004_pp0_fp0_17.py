import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# this is a function that returns a function pointer
getfunc = lib.getfunc
getfunc.restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# getfunc returns a function pointer that takes an integer argument
# and returns an integer
func = getfunc()
print func(1)

# func is a function pointer, so we can pass it to another function
# that takes a function pointer as an argument
lib.callfunc(func, 1)

# we can also assign it to a function pointer variable
CALLFUNC = ctypes.CFUNCTYPE(None, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int)
callfunc = CALLFUNC(("callfunc", lib))
callfunc(func, 2)

# or to a ctypes array of function pointers
arraytype = ctypes.CFUNCTYPE(ctypes
