import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref

from test import support

# A mixin class to provide some tests common to all RawIOBase
# implementations.
class RawIOMixin:

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.io.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, b'')

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.io.write, b'')

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.io.seek, 0)

    def test_tell(self):
        self.assertRaises(io.UnsupportedOperation, self.io.tell)

    def test_truncate(self):
        self.assertRaises(io.UnsupportedOperation, self.io.truncate, 0)

    def test_fileno
