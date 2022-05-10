import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER
#
# The tests in this file check that a ctypes.CFUNCTYPE object
# can be passed to CDLL.LoadLibrary and CDLL.GetProcAddress
# and that it can be used to call the function.  They also check
# that a ctypes.POINTER(CFUNCTYPE) can be passed to CDLL.LoadLibrary
# and CDLL.GetProcAddress and that it can be used to call the
# function.
#
# This test requires a function 'testfunc' to be provided by the
# test harness.  This function must take four integer arguments,
# and return an integer result.
from ctypes import *

