import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the ctypes tutorial, which is
# Copyright (c) 2000-2001 Thomas Heller.  All rights reserved.
#
# Modified for Python 2.5 by Thomas Heller.
#
# This test is in the public domain.

import unittest
from test import test_support

import sys

if sys.platform == "win32":
    from ctypes import wintypes

# XXX This test is not yet complete.

class CFunctionTypeTestCase(unittest.TestCase):

    def test_simple(self):
        # Simple example:
        # int abs(int)
        from ctypes import c_int, CFUNCTYPE
        libc = cdll.msvcrt
        prototype = CFUNCTYPE(c_int, c_int)
        paramflags = (1, "x")
        abs = prototype(( "abs", libc ), paramflags)
        self.assertEqual(abs(-1), 1)
        self.assertEqual(abs(1), 1)

    def test_simple_2(self
