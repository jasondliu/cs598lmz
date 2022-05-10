import io
# Test io.RawIOBase

import unittest

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Issue #16061: calling read() with a negative argument should
        # raise a ValueError.
        class MockRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                return 0
        self.assertRaises(ValueError, MockRawIO().read, -1)

class RawIOBaseTest(unittest.TestCase):

    def test_readinto(self):
        # Issue #16061: calling readinto() with a negative argument
        # should raise a ValueError.
        class MockRawIO(io.RawIOBase):
            def readable(self):
                return True
            def read(self, n=-1):
                return bytes()
        self.assertRaises(ValueError, MockRawIO().readinto, bytearray())

class BufferedReaderTest(unittest.TestCase):

    def test_read_neg(self):
       
