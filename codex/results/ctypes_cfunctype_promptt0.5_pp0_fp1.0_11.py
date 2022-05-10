import ctypes
# Test ctypes.CFUNCTYPE with a function that returns void.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# void func(int)
func = lib.func
func.argtypes = (ctypes.c_int,)
func.restype = None

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int)

def callback(arg):
    print("callback", arg)

cb = CALLBACK(callback)

func(42)
func.restype = ctypes.c_int
print(func(42))
func.restype = None

# void func_callback(void (*func)(int), int)
func_callback = lib.func_callback
func_callback.argtypes = (CALLBACK, ctypes.c_int)
func_callback.restype = None

func_callback(cb, 42)
func_callback.restype = ctypes.c_int
print(func_callback(cb, 42))
func_callback.restype = None

# void func_callback
