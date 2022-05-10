import ctypes
# Test ctypes.CFUNCTYPE *args n **keywords with a python callable.

from ctypes import *
from ctypes.test.test_capi import check_implicit_conversions, check_int_through_ptr

f = CFUNCTYPE(c_int, c_char_p, POINTER(c_int))(len)
buf = c_buffer("abcdef")
p = f(buf, 0)
assert p.value == 6

# xxx fix this!
#f = CFUNCTYPE(c_int, c_char_p, POINTER(c_int))(len)
#f(buf, None)

def func(x, y, z):
    return "%s%s%s" % (x, y, z)

f = CFUNCTYPE(c_char_p, c_char_p, c_char_p, c_char_p)(func)
buf = c_buffer("abcdef")
assert f(buf, buf, buf) == "abcabcabc"

f = CFUNCTYPE(c_char_p,
