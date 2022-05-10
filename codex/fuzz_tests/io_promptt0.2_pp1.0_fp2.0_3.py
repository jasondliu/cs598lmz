import io
# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_calls += 1
                return super().readinto(b)
        buf = bytearray(b"abc")
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        self.assertEqual(rawio.readinto(buf), 0)
        self.assertEqual(rawio.readinto_calls, 1)
        self.assertEqual(buf, b"abc")
        rawio.readinto_calls = 0
        self.assertEqual(rawio.readinto(memoryview(buf)), 0)
        self.assertEqual(rawio.readinto_calls, 1)
        self.assertEqual(buf, b"abc")

    def test_readall(self):
        # Test Raw
