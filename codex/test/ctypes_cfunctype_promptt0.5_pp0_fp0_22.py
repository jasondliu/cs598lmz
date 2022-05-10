import ctypes
# Test ctypes.CFUNCTYPE
#
# This test creates a function pointer type, and then creates a
# function pointer of that type and calls it.

# This test is slightly different from test_callbacks.py, because
# the callback function is not a global function.

import sys

from ctypes import *

