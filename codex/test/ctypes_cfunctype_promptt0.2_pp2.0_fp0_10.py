import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of the ctypes.CFUNCTYPE() factory function.
# It is used to create callback functions.

from ctypes import *
import unittest

class CFUNCTYPETest(unittest.TestCase):
    def callback(self, *args):
        self.got_args = args
        return args[-1]

