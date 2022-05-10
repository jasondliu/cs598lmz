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
    print 'myfunc', n
    return n * 10

# call the function
res = lib.myfunc(myfunc, ctypes.c_int(42))
print res

# call a function with a function pointer argument

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the restype and argtypes
lib.myfunc.restype = ctypes.c_int
lib.myfunc.arg
