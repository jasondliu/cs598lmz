import ctypes
# Test ctypes.CFUNCTYPE with simple restype
from ctypes import *

test_func = CFUNCTYPE(c_int, c_int, c_int)(lambda a, b: a + b)
assert test_func(1, 2) == 3

# Test CFUNCTYPE with string restype
def str_test(x):
    return x.upper()

encoded = CFUNCTYPE(c_char_p)(str_test)
assert encoded(b"abc") == b"ABC"

# Test ctypes.byref() with simple type
from ctypes import *

x = c_int()
x.value = 100
byref(x).contents.value += 1
assert x.value == 101

# Test ctypes.byref() with pointer
from ctypes import *

x = c_int()
x.value = 100
p = pointer(x)
assert p.contents.value == 100
p.contents.value += 1
assert p.contents.value == 101
assert x.value == 101

# Test ctypes.byref() with
