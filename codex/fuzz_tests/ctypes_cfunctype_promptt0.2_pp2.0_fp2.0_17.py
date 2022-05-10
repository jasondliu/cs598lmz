import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x):
    return x * 2

CALLBACK = CFUNCTYPE(c_int, c_int)

callback = CALLBACK(func)

print callback(2)

if __name__ == "__main__":
    import sys
    ret = run_test(__name__, __file__)
    sys.exit(ret)
