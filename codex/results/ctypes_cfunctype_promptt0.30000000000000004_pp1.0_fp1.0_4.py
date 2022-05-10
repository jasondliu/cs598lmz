import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    return args

CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CFuncPtr(func)
print f(1, 2)

CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                            ctypes.c_int)

f = CFuncPtr(func)
print f(1, 2, 3)

CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                            ctypes.c_int, ctypes.c_int)

f = CFuncPtr(func)
print f(1, 2, 3, 4)

CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                            ctypes
