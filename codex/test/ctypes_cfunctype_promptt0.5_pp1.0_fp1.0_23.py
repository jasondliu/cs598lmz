import ctypes
# Test ctypes.CFUNCTYPE()
#
# This is a test to verify that ctypes.CFUNCTYPE(...) creates a type
# object with a correct __name__ attribute.
#
# More information:
# http://bugs.python.org/issue10726

import unittest
from ctypes import *

