import io
# Test io.RawIOBase.readinto()
# See http://bugs.python.org/issue17482

import unittest

class ReadintoTest(unittest.TestCase):

    def test_readinto_with_bytearray(self):
        # Issue 17482: io.RawIOBase.readinto() should work with bytearray
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:4] = b'1234'
                return 4
        r = MyRawIO()
        b = bytearray(4)
        n = r.readinto(b)
        self.assertEqual(n, 4)
        self.assertEqual(b, b'1234')

    def test_readinto_with_memoryview(self):
        # Issue 17482: io.RawIOBase.readinto() should work with memoryview
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:4] = b'1234'
                return 4
       
