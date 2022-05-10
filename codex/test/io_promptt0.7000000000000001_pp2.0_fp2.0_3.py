import io
# Test io.RawIOBase.read().

import unittest

class RawIOTestCase(unittest.TestCase):
    # TODO: add more tests

    def testRead(self):
        class testRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'a'*len(b)
                return len(b)
        rawio = testRawIO()
        self.assertEqual(rawio.read(1), b'a')
        self.assertEqual(rawio.read(9), b'a'*9)
        self.assertEqual(rawio.read(100), b'a'*100)
        self.assertEqual(rawio.read(1000), b'a'*1000)

    def testReadAll(self):
        # Issue #6337
        class TestRawIO(io.RawIOBase):
            def __init__(self):
                self.read_count = 0
            def readinto(self, b):
                n = len(b)
                i = self.read_count
