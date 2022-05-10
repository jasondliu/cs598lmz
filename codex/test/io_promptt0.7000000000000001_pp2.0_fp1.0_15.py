import io
# Test io.RawIOBase
import io
import unittest

class RawIOTests(unittest.TestCase):

    def setUp(self):
        self.rawio = io.RawIOBase()

    def test_interfaces(self):
        # RawIOBase is a context manager
        self.assertRaises(TypeError, self.rawio.__enter__)
        self.assertRaises(TypeError, self.rawio.__exit__, None, None, None)
        self.assertRaises(TypeError, self.rawio.readinto, bytearray())
        self.assertRaises(TypeError, self.rawio.read, 0)
        self.assertRaises(TypeError, self.rawio.write, b"")

    def test_attributes(self):
        self.assertIsNone(self.rawio.mode)
        self.assertRaises(UnsupportedOperation, setattr, self.rawio, "mode",
                          "r")

