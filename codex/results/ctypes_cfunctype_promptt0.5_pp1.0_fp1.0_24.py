import ctypes
# Test ctypes.CFUNCTYPE
#
# The code below is a modified version of code from the ctypes tutorial,
# see http://starship.python.net/crew/theller/ctypes/tutorial.html
#
# The original code was written by Thomas Heller, and is released under
# the PSF license. 
#

from ctypes import *

# Load the DLL manually to ensure that it is loaded before the test runs.
# This is a workaround for an apparent bug in Python 2.4 on Windows.
# See http://bugs.python.org/issue1628884
ctypes.cdll.msvcrt

import unittest
from test import test_support

class CFuncPtrTest(unittest.TestCase):

    def test_pointer(self):
        # load the dll
        dll = cdll.msvcrt

        # set argtypes/restype for a function
        prototype = CFUNCTYPE(c_int, c_int)
        paramflags = (1, "value")
        cmp = prototype((("cmp", dll), paramflags))

       
