import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this function is declared as:
# void func(int (*callback)(int))

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print("callback called with", value)
    return value + 1

func = lib.func
func.argtypes = (CALLBACK,)
func.restype = None

func(CALLBACK(callback))

# call a function with a function pointer argument
# this function is declared as:
# int func(int (*callback)(int, int), int arg)

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(value, arg):
    print("callback called with", value, arg)
    return value + arg

func = lib.func2
func.argtypes
