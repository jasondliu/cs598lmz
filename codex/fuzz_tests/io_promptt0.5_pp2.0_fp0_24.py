import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns None, and doesn't raise an exception.
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return None

        self.assertIsNone(MyRawIO().readinto(b''))

    def test_readinto_error(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                raise OSError()

        # Read into a bytearray.
        self.assertRaises(OSError, MyRawIO().readinto, bytearray(5))

        # Read into a memoryview.
        self.assertRaises(OSError, MyRawIO().readinto, memoryview(bytearray(5)))

    def test_readinto_overflow(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return 99999

        self.assertRaises(OverflowError
