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

dll = CDLL(util.find_library("m"))
func = dll._testfunc_p_dfPCw
func.restype = restype
func.argtypes = argtypes

# Test for a simple int
@callback
def func_callback(a, b, c, d):
    print 'func_callback', a, b, c, d
    return a

func(2.5, 3.5,
