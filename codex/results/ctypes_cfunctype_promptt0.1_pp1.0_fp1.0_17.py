import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
#
# prototype:
#   int func(int (*callback)(int))
#
# callback:
#   int callback(int)

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print("callback called with", value)
    return value + 1

CALLBACK = CALLBACKFUNC(callback)

func = lib.func
func.argtypes = (CALLBACKFUNC,)
func.restype = ctypes.c_int

print(func(CALLBACK))

# call a function with a function pointer argument
#
# prototype:
#   int func2(int (*callback)(void *, int), void *userdata)
#
# callback:
#   int callback(void *, int)

CALLBACKFUNC2 = ctypes.CFUNCTYPE(ctypes.
