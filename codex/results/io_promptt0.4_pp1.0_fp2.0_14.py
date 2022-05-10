import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:3] = b'foo'
                return 3
        r = MyRawIO()
        b = bytearray(5)
        n = r.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b'foo\x00\x00')
        b = bytearray(3)
        n = r.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b'foo')
        b = bytearray(2)
        n = r.readinto(b)
        self.assertEqual(n, 2)
        self.assertEqual(b, b'fo')
        b = bytearray(1)
        n = r.readinto(b)
        self.assertEqual(n, 1
