import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)

# call_func is a CFUNCTYPE instance, call_func(42, 43) should return 42+43
call_func = ctypes.CFUNCTYPE(restype, *argtypes)(("call_func", lib), argtypes)

# call_func_ex is a CFUNCTYPE instance, call_func_ex(42, 43) should return 42*43
call_func_ex = ctypes.CFUNCTYPE(restype, *argtypes)(("call_func_ex", lib), argtypes)

# call_func_gen is a CFUNCTYPE instance, call_func_gen(42, 43) should return 42+43
call_func_gen = ctypes.CFUNCTYPE(restype, *argtypes)(("call_func_gen", lib), argtypes)

# call_
