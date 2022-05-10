import io
# Test io.RawIOBase
io.RawIOBase()

class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() doesn't return the number of bytes read.
        class MyRawIOBase(io.RawIOBase):
            def readinto(self, b):
                return 42

        raw = MyRawIOBase()
        b = bytearray(1)
        self.assertEqual(raw.readinto(b), None)
        self.assertEqual(b, b'\x00')

    def test_readinto_non_integral_n(self):
        # Test that readinto() handles non-integral buffer sizes.
        class MyRawIOBase(io.RawIOBase):
            def readinto(self, b):
                return len(b)

        raw = MyRawIOBase()
        b = memoryview(bytearray(1))
        self.assertEqual(raw.readinto(b), 1)
        self.assertEqual(b, b'\x00')

    def test_
