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
        # Test that readinto() raises a TypeError if the object it
        # is passed cannot be used to hold bytes.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                self.readinto_called = True
                return None
        raw = TestRawIO()
        self.assertRaises(TypeError, raw.readinto, 10)
        self.assertFalse(hasattr(raw, 'readinto_called'))

    def test_readall(self):
        #
