import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import weakref
import errno
import _io
import _testcapi

from test import support

# Base class for testing io.RawIOBase.
# The child class should define a setUp method defining self.thetype.
class BaseRawTests:

    # This is a class attribute so that it can be overridden in the
    # child class.
    _delete_warnings = True

    def setUp(self):
        self.f = self.thetype(b"")
        self.f._checkClosed = lambda: None

    def tearDown(self):
        if self._delete_warnings:
            support.check_warnings(self)
        self.f.close()
        self.assertRaises(ValueError, self.f.fileno)

    def test_constructor(self):
        self.assertRaises(TypeError, self.thetype)

    def test_read(self):
        self.assertRaises(NotImplementedError, self.f.read)

   
