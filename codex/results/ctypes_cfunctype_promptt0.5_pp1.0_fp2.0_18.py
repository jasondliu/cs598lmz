import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import _ctypes_test

def func(*args):
    print(args)

FUNC = ctypes.CFUNCTYPE(None, *([ctypes.c_int] * 10))
f = FUNC(func)
f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

f = FUNC(None, func)
f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

f = FUNC(None, None, func)
f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

f = FUNC(None, None, None, func)
f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

f = FUNC(None, None, None, None, func)
f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

f = FUNC(None, None, None, None, None, func)
f(1
