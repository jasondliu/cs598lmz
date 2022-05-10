import io
# Test io.RawIOBase

import io
import _pyio as pyio
import unittest

# A dummy raw stream class
class DummyRawIO(io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        return 0
    def write(self, b):
        return 0

class TestRawIO(unittest.TestCase):

    def test_init(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        f = DummyRawIO()
        self.assertRaises(TypeError, f.read)

    def test_readall(self):
        f = DummyRawIO()
        self.assertRaises(TypeError, f.readall)

    def test_readinto(self):
        f = DummyRawIO()
        self.assertRaises(TypeError, f.readinto, b"")

    def test_readline(self
