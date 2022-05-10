import ctypes
# Test ctypes.CFUNCTYPE

# This test is a bit special, because it doesn't really test the
# library, but the ctypes module itself.

# The CFUNCTYPE class is used as a base class for the rest of the
# ctypes classes.  It implements the __call__ method, which is used
# to call the function.

import unittest
from ctypes import *
