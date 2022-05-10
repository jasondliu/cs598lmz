import ctypes
# Test ctypes.CFUNCTYPE

# This is a simple test to check that ctypes.CFUNCTYPE works.

import ctypes
from ctypes import *

def check(result, func, args):
    got = func(*args)
    if result != got:
        print(func)
        print(args, "->", got, "expected:", result)
        raise Exception("wrong result")

# Simple function types

f = CFUNCTYPE(c_int, c_int)(lambda x: x + 42)
check(43, f, (1,))
check(42, f, (0,))

f = CFUNCTYPE(c_int, c_int, c_int)(lambda x, y: x + y)
check(43, f, (1, 42))
check(42, f, (0, 42))

f = CFUNCTYPE(c_int, c_int, c_int, c_int)(lambda x, y, z: x + y + z)
check(43, f, (1, 40, 2))
