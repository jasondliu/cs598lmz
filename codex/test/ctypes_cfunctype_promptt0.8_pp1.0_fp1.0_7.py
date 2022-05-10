import ctypes
# Test ctypes.CFUNCTYPE.
from ctypes import *
import sys

# test whether we are using the Microsoft C runtime, or not
# (the test is quite heuristic...)

do_msvc_test = True
