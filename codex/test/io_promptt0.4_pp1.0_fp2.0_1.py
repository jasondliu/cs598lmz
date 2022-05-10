import io
# Test io.RawIOBase

import unittest

class RawIOBaseTest(unittest.TestCase):

    def test_readinto(self):
        # Issue #27397: check that readinto() accepts a memoryview.
        b = bytearray(10)
        m = memoryview(b)
        f = io.BytesIO(b'0123456789')
        n = f.readinto(m)
        self.assertEqual(n, 10)
        self.assertEqual(b, b'0123456789')

    def test_readinto_resize(self):
        # Issue #27397: check that readinto() resizes the memoryview.
        b = bytearray(5)
        m = memoryview(b)
        f = io.BytesIO(b'0123456789')
        n = f.readinto(m)
        self.assertEqual(n, 5)
        self.assertEqual(b, b'01234')

