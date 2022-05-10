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
                return len(b)
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        b = bytearray(b'abc')
        self.assertEqual(rawio.readinto(b), 3)
        self.assertEqual(b, b'abc')
        self.assertEqual(rawio.readinto_calls, 1)
        self.assertEqual(rawio.readinto(b, 1), 3)
        self.assertEqual(b, b'aabc')
        self.assertEqual(rawio.readinto_calls, 2)
        self.assertEqual(rawio.readinto(b, 1, 1), 3)
        self.assertEqual(
