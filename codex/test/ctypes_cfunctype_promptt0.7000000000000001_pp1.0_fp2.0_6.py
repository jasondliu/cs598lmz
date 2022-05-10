import ctypes
# Test ctypes.CFUNCTYPE with simple restype
from ctypes import *

test_func = CFUNCTYPE(c_int, c_int, c_int)(lambda a, b: a + b)
assert test_func(1, 2) == 3

# Test CFUNCTYPE with string restype
def str_test(x):
    return x.upper()

encoded = CFUNCTYPE(c_char_p)(str_test)
