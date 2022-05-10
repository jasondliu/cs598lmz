import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call_function takes a function pointer and calls it
call_function = lib.call_function
call_function.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),)
call_function.restype = ctypes.c_int

# call_function_obj takes a function object and calls it
call_function_obj = lib.call_function_obj
call_function_obj.argtypes = (ctypes.py_object,)
call_function_obj.restype = ctypes.c_int

# call_function_va takes a function pointer and calls it
call_function_va = lib.call_function_va
call_function_va.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int),)
call_function_va.restype = ctypes.c_int

# call_function_va
