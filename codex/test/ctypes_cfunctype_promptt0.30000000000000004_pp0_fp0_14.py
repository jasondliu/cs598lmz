import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import _ctypes_test

def func(*args):
    print(args)
    return args[-1]

CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CFuncPtr(func)
print(f(1, 2))

f = CFuncPtr(lambda x, y: x + y)
print(f(1, 2))

f = CFuncPtr(lambda x, y: x + y, use_errno=True)
print(f(1, 2))

f = CFuncPtr(lambda x, y: x + y, use_last_error=True)
print(f(1, 2))

f = CFuncPtr(lambda x, y: x + y, use_errno=True, use_last_error=True)
print(f(1, 2))

