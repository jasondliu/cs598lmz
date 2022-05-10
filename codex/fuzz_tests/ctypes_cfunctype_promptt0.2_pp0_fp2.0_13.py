import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer parameter
#
# int func(int (*callback)(int))

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print('callback called with', value)
    return value + 1

CALLBACK = CALLBACKFUNC(callback)

func = lib.func
func.argtypes = (CALLBACKFUNC,)
func.restype = ctypes.c_int

res = func(CALLBACK)
print(res)

# call a function with a function pointer parameter
#
# int func2(int (*callback)(int, int), int arg)

CALLBACKFUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback2(value, arg):
    print('callback2 called with', value,
