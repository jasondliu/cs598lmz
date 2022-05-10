import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno

from test import test_support

# A mixin for testing RawIOBase objects.
class RawIOMixin(object):
    # This is a mixin for testing RawIOBase objects.  It doesn't define
    # any tests of its own, but it defines setUp(), which defines
    # self.thetype, the type object being tested.  It also defines
    # self.filename, which is the name of a file that can be used for
    # testing (self.thetype must accept a filename parameter).

    def setUp(self):
        self.thetype = io.RawIOBase
        self.filename = test_support.TESTFN

    def test_attributes(self):
        # Check attributes.
        rawio = self.thetype(self.filename)
        self.assertEqual(rawio.mode, 'rb+')
        rawio.close()
        self.assertRaises(ValueError, getattr, rawio, 'mode')

    def test_
