import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Test readinto()
        class TestRawIO(io.RawIOBase):
            def __init__(self):
                self.readinto_calls = 0
            def readinto(self, b):
                self.readinto_calls += 1
                self.readinto_b = b
                return len(b)
        raw = TestRawIO()
        b = bytearray(10)
        n = raw.readinto(b)
        self.assertEqual(n, 10)
        self.assertEqual(raw.readinto_calls, 1)
        self.assertEqual(raw.readinto_b, b)
        n = raw.readinto(memoryview(b))
        self.assertEqual(n, 10)
        self.assertEqual(raw.readinto_calls, 2)
        self.assertEqual(raw.readinto_b, b)
        self.assertRaises(TypeError, raw.readinto
