import ctypes
# Test ctypes.CFUNCTYPE
import os
import sys
import unittest
import _ctypes_test
from _ctypes_test import get_errno
import _ctypes
from ctypes import *
from ctypes.util import find_library
import _rawffi

if sys.platform == "win32":
    from _ctypes_test import get_last_error

libc_name = find_library("c")
if libc_name is None:
    raise unittest.SkipTest("Could not find C library")

libc = CDLL(libc_name)

def callback(arg):
    return arg

CALLBACK = CFUNCTYPE(c_int, c_int)

class CFuncPtrTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(callback(42), 42)

    def test_callbacks(self):
        cb = CALLBACK(callback)
        self.assertEqual(cb(42), 42)

    def test_errcheck(self):
        def errcheck(result,
