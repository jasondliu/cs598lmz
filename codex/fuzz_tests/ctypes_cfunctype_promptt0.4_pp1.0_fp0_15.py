import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function taking a function pointer as argument
# and returning a function pointer
restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib.pass_func_ptr.restype = restype
lib.pass_func_ptr.argtypes = (restype,)

# a function taking a function pointer as argument
# and returning a function pointer
restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib.pass_func_ptr.restype = restype
lib.pass_func_ptr.argtypes = (restype,)


def func(n):
    print('func', n)
    return n + 1

f = lib.pass_func_ptr(func)
f(42)

# a function taking a function pointer as argument
# and returning a function pointer
restype = ctypes.CFUNCTYPE(ctypes.c_
