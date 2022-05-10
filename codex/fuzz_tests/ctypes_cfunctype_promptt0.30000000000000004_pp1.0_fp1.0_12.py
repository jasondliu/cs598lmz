import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x, y):
    return x + y

# CFUNCTYPE(restype, *argtypes)
Add = CFUNCTYPE(c_int, c_int, c_int)(func)
print Add(2, 3)

# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
AddError = CFUNCTYPE(c_int, c_int, c_int, use_errno=True)(func)
print AddError(2, 3)

# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
AddLastError = CFUNCTYPE(c_int, c_int, c_int, use_last_error=True)(func)
print AddLastError(2, 3)

# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
AddErrorLastError = CFUNCTY
