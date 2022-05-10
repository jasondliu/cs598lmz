import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer is created using CFUNCTYPE

# int func(int (*callback)(int))
func = lib.func
func.restype = ctypes.c_int
func.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),

def callback(value):
    print("callback", value)
    return value + 1

print(func(callback))

# call a function with a function pointer argument
# the function pointer is created using CFUNCTYPE
# and passed as keyword argument

# int func2(int (*callback)(int))
func2 = lib.func2
func2.restype = ctypes.c_int
func2.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),

print(func2(callback=callback))

# call a function with a function pointer
