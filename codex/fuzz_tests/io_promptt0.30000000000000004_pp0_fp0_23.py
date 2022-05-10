import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns None or raises OSError
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                pass
        self.assertIsNone(TestRawIO().readinto(bytearray(1)))
        self.assertRaises(OSError, TestRawIO().readinto, memoryview(bytearray(1)))
        self.assertRaises(TypeError, TestRawIO().readinto, bytearray())

    def test_readall(self):
        # Test that readall() returns None or raises OSError
        class TestRawIO(io.RawIOBase):
            def readall(self):
                pass
        self.assertIsNone(TestRawIO().readall())

    def test_read(self):
        # Test that read() returns None or raises OSError
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                pass
