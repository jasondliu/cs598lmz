import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the ctypes tutorial by Thomas Heller.
# http://starship.python.net/crew/theller/ctypes/tutorial.html
#
# The original tutorial is in the public domain.
#
# The test is written by Thomas Heller and modified by Martin v. Löwis.
# It is in the public domain.

import unittest
from test import test_support

import ctypes

# The following declaration is needed for the test to work on 64-bit
# platforms.  The test should work without it, but it doesn't.
# See http://bugs.python.org/issue14296
ctypes.c_longlong._type_ = "q"

class CFuncPtrTestCase(unittest.TestCase):
    def test_simple(self):
        # This test is based on the ctypes tutorial by Thomas Heller.
        # http://starship.python.net/crew/theller/ctypes/tutorial.html
        #
        # The original tutorial is in the public domain.
        #
        # The test is written
