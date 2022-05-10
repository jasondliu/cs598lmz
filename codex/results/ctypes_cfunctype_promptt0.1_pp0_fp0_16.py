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
func = prototype((restype, argtypes), ((1, "a"),))

# the function to pass as argument
def funcptr(a):
    return a + 1

# call the function in the dll
res = lib.call_function(func, 1)
print(res)
assert res == 2

# call the function in the dll
res = lib.call_function(funcptr, 1)
print(res)
assert res == 2

# call a function with a function pointer argument

# prototype of the function in the dll
prototype = ctypes.CFUNCTYPE(ctypes.c_int, c
