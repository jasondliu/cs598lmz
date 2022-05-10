import ctypes
# Test ctypes.CFUNCTYPE
#
# The purpose of this test is to test the ability of ctypes to call a
# function with the signature defined by CFUNCTYPE.

from ctypes import *

# If a platform does not have a 64-bit int, the types for long long,
# and long double are defined to be in the same range as int and
# double, respectively.
try:
    c_longlong
except NameError:
    c_longlong = c_long

try:
    c_longdouble
except NameError:
    c_longdouble = c_double

#
# Test functions with composite return values.
#

# This test checks if the return value is stored in the buffer passed
# as first argument.

def test_struct_result(func, argstype):
    class X(Structure):
        _fields_ = [("a", c_int),
                    ("b", c_int)]
    arg = argstype()
    arg.a = 10
    arg.b = 20
    x = func(byref(arg))
