import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support

# A mixin class for RawIOBase tests
class RawIOMixin:

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.io.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, bytearray())

    def test_readline(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readline)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.io.write, b'')

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.io.seek, 0)

    def test_tell(self):
        self.assertRaises(io.UnsupportedOperation, self.io.tell)

    def test_truncate(self):
        self.assertRaises(io.UnsupportedOperation, self.
