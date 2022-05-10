import ctypes
# Test ctypes.CFUNCTYPE()
from ctypes import *
import _ctypes_test

try:
    ctypes.pythonapi
except AttributeError:
    raise Exception("This test requires Python 2.5 or later")

# This test is only runnable on Windows.  It tests the
# ctypes.WINFUNCTYPE() function.

