import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:3] = b'foo'
                return 3

        rawio = TestRawIO()
        b = bytearray(5)
        n = rawio.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b'foo\x00\x00')
        n = rawio.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(b, b'foo\x00\x00')

    def test_readinto_non_writable(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:3] = b'foo'
                return 3

        rawio = TestRawIO()
        b = memoryview(bytearray(
