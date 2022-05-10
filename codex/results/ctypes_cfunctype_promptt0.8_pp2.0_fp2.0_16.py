import ctypes
# Test ctypes.CFUNCTYPE usage.

from ctypes import *

def compare(s, x, y):
    print(s, repr(x), repr(y))
    return -1

cmp_func = CFUNCTYPE(c_int, c_char_p, c_char_p)(compare)
print(cmp_func(b"a", b"b"))

try:
    cmp_func(b"a", 5)
except TypeError as e:
    print(e)

try:
    cmp_func(5, 6)
except TypeError as e:
    print(e)
