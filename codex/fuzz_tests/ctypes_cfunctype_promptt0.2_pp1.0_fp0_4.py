import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
#
# int func(int (*)(int))

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 1

func = lib.func
func.argtypes = (CALLBACK,)
func.restype = ctypes.c_int

res = func(CALLBACK(callback))
print("func returned", res)

# call a function with a function pointer argument
#
# int func2(int (*)(int, void *), void *)

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

def callback(arg, data):
    print("callback called with", arg, data)
    return arg + 1

func = lib.func2

