import io
# Test io.RawIOBase

class RawIOBaseTest(unittest.TestCase):

    def test_readinto(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:3] = b"foo"
                return 3
        f = TestRawIO()
        b = bytearray(5)
        n = f.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"foo\x00\x00")

    def test_readinto_non_integral(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return None
        f = TestRawIO()
        b = bytearray(5)
        self.assertRaises(TypeError, f.readinto, b)

    def test_readinto_negative(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return -1
        f = TestRawIO()

