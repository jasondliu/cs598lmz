import ctypes
# Test ctypes.CFUNCTYPE for multiple return values
from ctypes import *

def callback(*args):
    return args

functype = CFUNCTYPE(c_int, c_int, c_int, c_int)

## Prototype: int func(int a, int b, int c);
func = functype(callback)

