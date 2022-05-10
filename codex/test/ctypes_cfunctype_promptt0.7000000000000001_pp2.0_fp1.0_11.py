import ctypes
# Test ctypes.CFUNCTYPE

#
# This test is based on a test from the ctypes testsuite, which is
# available as "run_all.py" in the ctypes source distribution.
#

from ctypes import *

# c_int, c_double, c_char_p
try:
    c_wchar
except NameError:
    c_wchar = c_short

callback = CFUNCTYPE(c_int, c_int, c_double, c_char_p, c_wchar)

restype = c_double
argtypes = (c_int, c_double, c_char_p, c_wchar)

