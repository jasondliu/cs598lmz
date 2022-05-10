import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns None.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                self.readinto_called = True
                return None
        raw = TestRawIO()
        b = bytearray(10)
        self.assertIsNone(raw.readinto(b))
        self.assertTrue(raw.readinto_called)

    def test_readinto_error(self):
        # Test that readinto() raises an error if the argument is not a
        # bytearray.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                pass
        raw = TestRawIO()
        self.assertRaises(TypeError, raw.readinto, memoryview(b''))

    def test_readall(self):
        # Test that readall() returns None.
        class TestRawIO(io.RawIOBase):
            def readall(self):
