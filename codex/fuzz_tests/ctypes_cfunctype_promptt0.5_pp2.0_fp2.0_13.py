import ctypes
# Test ctypes.CFUNCTYPE with a function pointer

import ctypes
from ctypes import *

def func(a, b):
    return a + b

def test(FuncType, func, paramflags):
    FuncPtr = FuncType(func)
    FuncPtr.paramflags = paramflags
    res = FuncPtr(1, 2)
    print(res)

if __name__ == "__main__":
    test(CFUNCTYPE(c_int, c_int, c_int), func, (1, 1, 0))
