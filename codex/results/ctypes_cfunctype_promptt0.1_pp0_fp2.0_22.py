import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer is created with CFUNCTYPE

# int func(int (*callback)(int))
func = lib.func
func.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),)
func.restype = ctypes.c_int

# int callback(int)
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print("callback called with", value)
    return value + 1

print(func(CALLBACK(callback)))

# call a function with a function pointer argument
# the function pointer is created with CFUNCTYPE
# and passed as keyword argument

# int func2(int (*callback)(int))
func2 = lib.func2
func2.argtypes = (ctypes.CFUNCTYPE(ctypes.
