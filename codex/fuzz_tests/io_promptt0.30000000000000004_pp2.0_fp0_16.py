import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
import weakref

from test import support

# Test RawIOBase using a StringIO object

class TestRawIO(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_attributes(self):
        rawio = io.BytesIO()
        self.assertEqual(rawio.mode, 'wb+')
        rawio = io.BytesIO(b"blah")
        self.assertEqual(rawio.mode, 'wb+')
        self.assertEqual(rawio.name, None)

    def test_rawio_close(self):
        rawio = io.BytesIO()
        rawio.close()
        self.assertTrue(rawio.closed)
        rawio.close()
        self.assertTrue(rawio.closed)

    def test_rawio_closed_attribute(self):
        rawio = io.BytesIO()
        self.assert
