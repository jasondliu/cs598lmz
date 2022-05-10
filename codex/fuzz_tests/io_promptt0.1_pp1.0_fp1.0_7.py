import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings

from test import support

# Base class for testing a RawIOBase implementation.
# Subclasses must override read(), readinto() and seek().
class BaseRawIOBaseTests(object):

    def test_constructor(self):
        # No public constructor.
        self.assertRaises(TypeError, io.RawIOBase)

    def test_attributes(self):
        # RawIOBase defines a number of public attributes.
        rawio = self.MockRawIO()
        self.assertEqual(rawio.mode, None)
        self.assertEqual(rawio.name, None)
        self.assertEqual(rawio.closed, False)
        rawio.close()
        self.assertEqual(rawio.closed, True)

    def test_read(self):
        # read() should return a bytes object.
        rawio = self.MockRawIO()
        self.assertEqual(rawio.read(), b'')

