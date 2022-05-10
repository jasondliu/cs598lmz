import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype of the function in the dll
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function in the dll
restype = ctypes.c_int
argtypes = (ctypes.c_int,)
func = prototype((restype, argtypes),
                 (lib, 'add_one'))

# the function to pass to the dll function
def add_one(n):
    return n + 1

# call the dll function
res = lib.call_with_funcptr(func, 1)
print(res)
assert res == 2

# call a function with a function pointer argument
# and a user data pointer

# prototype of the function in the dll
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

#
