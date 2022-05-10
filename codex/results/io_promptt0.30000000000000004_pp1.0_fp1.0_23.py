import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Issue #16791: io.RawIOBase.readinto() should return None
        # if the argument is 0-length.
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return None
        self.assertIsNone(MyRawIO().readinto(b''))
        self.assertIsNone(MyRawIO().readinto(memoryview(b'')))
        self.assertIsNone(MyRawIO().readinto(bytearray()))

    def test_readinto_with_negative_argument(self):
        # Issue #16791: io.RawIOBase.readinto() should raise ValueError
        # if the argument is negative.
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return None
        self.assertRaises(ValueError, MyRawIO().readinto, b'\x00'*(-1))
        self.assertRaises(ValueError
