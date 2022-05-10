import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
import _ctypes_test

# Issue #6: ctypes.CFUNCTYPE(c_int) was not callable.
#
# This is fixed by patch #7

