import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

import _ctypes_test

################################################################
#
# ensure no segfault when trying to print non-printable character
#

c_int = ctypes.c_int
c_char_p = ctypes.c_char_p

faulty = c_char_p(b"\xcc\xcc\xcc\xcc\xcc")
good = c_char_p(b"hello\x00")
default = c_int(-123456)

try:
    c_int.in_dll(_ctypes_test, "faulty")
except ValueError:
    pass

try:
    c_int.in_dll(_ctypes_test, "good")
except ValueError:
    pass

try:
    c_int.in_dll(_ctypes_test, "doesnt_exist")
except ValueError:
    pass

assert c_int.in_dll(_ctypes_test, "default") == default

#
#
################################################################
