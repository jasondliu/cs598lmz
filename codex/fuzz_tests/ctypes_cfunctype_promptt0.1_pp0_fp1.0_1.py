import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer is created with CFUNCTYPE

# int func(int (*callback)(int))
func = lib.func
func.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
func.restype = ctypes.c_int

# int callback(int)
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print('callback called with', value)
    return value + 1

# call func(callback)
res = func(CALLBACK(callback))
print('func returned', res)

# call func(None)
res = func(None)
print('func returned', res)

# call func(42)
try:
    res = func(42)
except TypeError:
    print('calling func(42) raises TypeError
