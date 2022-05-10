import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE, and also a test of the
# ctypes.c_void_p type.

import unittest
from ctypes import *

class CFuncPtrTestCase(unittest.TestCase):
    def test_basic(self):
        # This is a basic test of ctypes.CFUNCTYPE.

        # The CFUNCTYPE() constructor creates a C function pointer type.
        # The first argument is the return type, the rest are the
        # argument types.
        #
        # The function pointer type can be called like a Python
        # callable.  The arguments to the Python call are converted
        # according to the argument types given to CFUNCTYPE(), and the
        # return value is converted according to the return type.
        #
        # CFUNCTYPE() can also be called with an optional first argument
        # which specifies which calling convention is to be used.  The
        # default calling convention is platform-specific.

        # The c_void_p type is used to represent a pointer.
