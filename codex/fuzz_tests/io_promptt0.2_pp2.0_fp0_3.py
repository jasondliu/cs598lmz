import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto(self):
        # Issue #17091: io.RawIOBase.readinto() should return None
        # when the argument is too small.
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return None
        self.assertIsNone(MyRawIO().readinto(bytearray(1)))

    def test_readinto_error(self):
        # Issue #17091: io.RawIOBase.readinto() should raise
        # TypeError when the argument is not a writable buffer.
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return None
        self.assertRaises(TypeError, MyRawIO().readinto, 1)

    def test_readinto_negative(self):
        # Issue #17091: io.RawIOBase.readinto() should raise
        # ValueError when the argument has a negative length.
        class MyRaw
