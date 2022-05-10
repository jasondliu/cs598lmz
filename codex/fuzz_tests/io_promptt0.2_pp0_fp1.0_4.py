import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns the correct number of bytes
        # read, and doesn't modify the buffer past that.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:2] = b'xy'
                return 2
        b = bytearray(5)
        self.assertEqual(TestRawIO().readinto(b), 2)
        self.assertEqual(b, b'xy\x00\x00\x00')
        self.assertEqual(TestRawIO().readinto(b[2:]), 0)
        self.assertEqual(b, b'xy\x00\x00\x00')
        self.assertEqual(TestRawIO().readinto(b), 0)
        self.assertEqual(b, b'xy\x00\x00\x00')
        self.assertEqual(TestRawIO().readinto(b[2:]), 0)

