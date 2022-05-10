import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support

# A mixin for RawIOBase tests that provides some utility functions
# and checks for the attributes that RawIOBase defines.
class RawIOMixin:

    def test_attributes(self):
        rawio = self.MockRawIO()
        self.assertEqual(rawio.mode, None)
        self.assertEqual(rawio.name, None)
        self.assertEqual(rawio.closed, False)
        rawio.close()
        self.assertEqual(rawio.closed, True)

    def test_read(self):
        rawio = self.MockRawIO(b'abc')
        self.assertEqual(rawio.read(2), b'ab')
        self.assertEqual(rawio.read(2), b'c')
        self.assertEqual(rawio.read(2), b'')
        self.assertEqual(rawio.read(2), b'')
        self.assertEqual(rawio
