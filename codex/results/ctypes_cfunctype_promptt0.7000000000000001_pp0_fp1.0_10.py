import ctypes
# Test ctypes.CFUNCTYPE
from ctypes.test import need_symbol

from ctypes import *

import unittest

from ctypes.test import need_symbol
from ctypes.test.test_utils import import_module

from sys import getrefcount as grc

import _ctypes_test

################################################################
#
# These tests require a function in a system library, or in _ctypes_test.
#

class CFuncPtrTestCase(unittest.TestCase):

    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def check_type(self, argtypes, restype=None, errcheck=None):
        prototype = CFUNCTYPE(*argtypes)
        if restype is not None:
            prototype.restype = restype
        if errcheck is not None:
            prototype.errcheck = errcheck

        res = prototype(self.callback)
        self.assertEqual(len(self.got_args), len(argtypes))
        for got, expected in zip(self.got_
