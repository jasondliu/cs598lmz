import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test that read() returns empty bytes object at EOF
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                self.readinto_calls += 1
                return 0
        raw = TestRawIO()
        raw.readinto_calls = 0
        self.assertEqual(raw.read(), b'')
        self.assertEqual(raw.readinto_calls, 1)
        self.assertEqual(raw.read(), b'')
        self.assertEqual(raw.readinto_calls, 2)
        self.assertEqual(raw.read(1), b'')
        self.assertEqual(raw.readinto_calls, 3)
        self.assertEqual(raw.read(1), b'')
        self.assertEqual(raw.readinto_calls, 4)
        self.assertEqual(raw.read(-1),
