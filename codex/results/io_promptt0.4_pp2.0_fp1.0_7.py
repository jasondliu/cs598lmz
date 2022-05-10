import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_weakref(self):
        f = io.RawIOBase()
        p = weakref.proxy(f)
        self.assertRaises(TypeError, len, p)

    def test_read(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)

    def test_readinto(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())

    def test_write(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.write, b'')

    def test_close(self):
        f = io.RawIOBase()
        f.close()
        self.assertRaises(ValueError, f.fileno)

    def test_context_manager(self):
       
