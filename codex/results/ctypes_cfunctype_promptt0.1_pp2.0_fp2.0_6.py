import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the restype and argtypes
lib.myfunc.restype = ctypes.c_int
lib.myfunc.argtypes = (prototype, ctypes.c_int)

# define the function
def myfunc(n):
    print 'myfunc called with', n
    return n * 10

# call the function
print lib.myfunc(myfunc, 42)

# call a function with a function pointer argument

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the restype and argtypes
lib.myfunc.restype = ctypes.c_int
lib.myfunc.argtypes = (prototype, ctypes.c
