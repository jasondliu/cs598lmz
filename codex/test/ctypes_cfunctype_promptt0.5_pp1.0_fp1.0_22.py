import ctypes
# Test ctypes.CFUNCTYPE()

# This function takes a function pointer as first argument
# and returns the same pointer.

# The function pointer must accept an integer argument and
# return an integer result.

# The function pointer must be callable from C.

import sys
import ctypes
from ctypes import *

if sys.platform == "win32":
    import _ctypes_test
    dll = CDLL(_ctypes_test.__file__)
    func = dll._testfunc_callback
