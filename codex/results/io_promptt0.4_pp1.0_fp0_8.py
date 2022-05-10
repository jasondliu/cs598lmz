import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os

from test import support

class TestRawIOBase(unittest.TestCase):

    def test_attributes(self):
        self.assertEqual(io.RawIOBase.closed, False)
        self.assertEqual(io.RawIOBase.mode, '')
        self.assertEqual(io.RawIOBase.name, '')
        self.assertEqual(io.RawIOBase.newlines, None)
        self.assertEqual(io.RawIOBase.encoding, None)
        self.assertEqual(io.RawIOBase.errors, None)
        self.assertEqual(io.RawIOBase.line_buffering, False)

    def test_abstract_methods(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().read()
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto(b'')
        with self.assertRaises(
