import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import _ctypes_test

def func(*args):
    print("func", args)
    return args[-1]

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CFunc(func)
print(f(1, 2))

f = CFunc(lambda x, y: x + y)
print(f(1, 2))

f = CFunc(lambda x, y: x + y)
print(f(1, 2))

f = CFunc(lambda x, y: x + y)
print(f(1, 2))

f = CFunc(lambda x, y: x + y)
print(f(1, 2))

f = CFunc(lambda x, y: x + y)
print(f(1, 2))

f = CFunc(lambda x, y: x + y)
print(f(1, 2))

f = CFunc(lambda x, y: x + y)

