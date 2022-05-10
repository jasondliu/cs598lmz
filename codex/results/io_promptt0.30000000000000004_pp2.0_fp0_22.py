import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns None.
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_called = True
                return None
        raw = TestRawIO()
        b = bytearray(5)
        self.assertIsNone(raw.readinto(b))
        self.assertTrue(raw.readinto_called)

    def test_readinto_non_integral_length(self):
        # Issue #17093: readinto() should accept non-integral buffer length.
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_called = True
                return len(b)
        raw = TestRawIO()
        b = bytearray(5.0)
        self.assertEqual(raw.readinto(b
