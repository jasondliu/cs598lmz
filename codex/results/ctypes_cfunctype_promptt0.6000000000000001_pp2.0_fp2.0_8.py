import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
from ctypes.test import needs_symbol

import _ctypes_test

try:
    dll = cdll.LoadLibrary(_ctypes_test.__file__)
except WindowsError:
    import os
    dll = cdll[os.path.join(os.path.dirname(__file__),
                            "ctypes_test.dll")]

import unittest
from test import support

class CFunctionTypeTestCase(unittest.TestCase):
    def test_simple_functype(self):
        # This code is executed at runtime, not at compile time!
        # So we must not use globals which are not yet initialized when
        # the test is run.
        #
        # Therefore we call dll.get_cfunc to get a function pointer, which
        # we then use to create a CFuncPtr instance.
        #
        # We can then call the function through the CFuncPtr instance.
        int_restype = ctypes.c_int
        int_argtypes = (ctypes.c
