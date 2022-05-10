import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# a function pointer in a structure
class S(ctypes.Structure):
    _fields_ = [("func", FUNC)]

# a function pointer in a union
class U(ctypes.Union):
    _fields_ = [("func", FUNC)]

# a function pointer in an array
FUNC_ARRAY = FUNC * 3

# a function pointer as a return value
def funcptr_retval(x):
    return FUNC(x)

# a function pointer as a parameter
def funcptr_param(x):
    lib.funcptr_param.argtypes = FUNC,
    lib.funcptr_param.restype = ctypes.c_int
    return lib.funcptr_param(x)

# a function pointer as a parameter to a function pointer
def funcptr_param_func
