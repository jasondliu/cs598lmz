import io
# Test io.RawIOBase.readinto()

import io
import unittest
import array

class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # basic functionality
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'1'
                return 1
        self.assertEqual(TestRawIO().readinto(bytearray(5)), 1)

        # incompatible array
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'12345'
                return len(b)
        with self.assertRaises(TypeError):
            TestRawIO().readinto(array.array('i', [0]))

        # readinto() returns 0
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return 0
        self.assertEqual(TestRawIO().readinto(bytearray()), 0)

        # readinto() returns -1
