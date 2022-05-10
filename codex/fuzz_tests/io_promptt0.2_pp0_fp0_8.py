import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns the correct number of bytes
        # read and that it does not modify the buffer past the number
        # of bytes read.
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                self.readinto_calls += 1
                return len(b)
        buf = bytearray(b'x' * 10)
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        self.assertEqual(rawio.readinto(buf), 10)
        self.assertEqual(rawio.readinto_calls, 1)
        self.assertEqual(buf, b'x' * 10)
        self.assertEqual(rawio.readinto(buf), 0)
        self.assertEqual(rawio.readinto_calls, 2)
        self.assertEqual(buf, b'x' * 10)
        self.assertEqual(raw
