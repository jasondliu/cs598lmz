import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto(self):
        # This is a fake file that returns a bytes object of the requested length
        class FakeRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'x' * len(b)
                return len(b)
            def readable(self):
                return True
        # Empty array
        buf = bytearray()
        f = FakeRawIO()
        self.assertEqual(f.readinto(buf), 0)
        self.assertEqual(buf, b'')
        # Non-empty array
        buf = bytearray(10)
        f = FakeRawIO()
        self.assertEqual(f.readinto(buf), 10)
        self.assertEqual(buf, b'x' * 10)
        # Read past the end of the array
        buf = bytearray(10)
        f = FakeRawIO()
        self.assertEqual(f.
