import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns the number of bytes read.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return b.__setitem__(slice(None), b'x')
        self.assertEqual(TestRawIO().readinto(bytearray(5)), 5)

    def test_readinto_non_integral(self):
        # Test that readinto() returns a non-integral number of bytes.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return b.__setitem__(slice(None), b'x') + 0.5
        self.assertEqual(TestRawIO().readinto(bytearray(5)), 5.5)

    def test_readinto_negative(self):
        # Test that readinto() returns a negative number of bytes.
        class TestRawIO(io.RawIOBase):
            def readinto(self
