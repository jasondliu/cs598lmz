import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call_function
# prototype: int call_function(int(*)(int), int)
call_function = lib.call_function
call_function.restype = ctypes.c_int
call_function.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
                          ctypes.c_int)

def func(value):
    return value + 1

assert call_function(func, 3) == 4

# call_function_obj
# prototype: int call_function_obj(int(*)(int), int)
call_function_obj = lib.call_function_obj
call_function_obj.restype = ctypes.c_int
call_function_obj.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
                              ctypes.c_int)

class Func:
    def __call__(self
