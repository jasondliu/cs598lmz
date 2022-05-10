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
        b = bytearray(5)
        self.assertEqual(raw.readinto(b), None)
        self.assertTrue(raw.readinto_called)
        # Test that readinto() raises an exception.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                self.readinto_called = True
                raise OSError
        raw = TestRawIO()
        b = bytearray(5)
        self.assertRaises(OSError, raw.readinto, b)
        self.assertTrue(raw.readinto_called)
        # Test that readinto() returns a value that is not None or the
        # length of the buffer.
        class TestRaw
