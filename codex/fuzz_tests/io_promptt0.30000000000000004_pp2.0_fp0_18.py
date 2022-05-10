import io
# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        # Test that readinto() returns None.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                self.readinto_called = True
                return None
        rawio = TestRawIO()
        b = bytearray(5)
        self.assertIsNone(rawio.readinto(b))
        self.assertTrue(rawio.readinto_called)

    def test_readinto_resize(self):
        # Test that readinto() resizes the buffer.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b"hello"
                return len(b)
        rawio = TestRawIO()
        b = bytearray(2)
        self.assertEqual(rawio.readinto(b), 5)
        self.assertEqual(b, b"hello")

    def test_readinto_error(self):

