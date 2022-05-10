import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):

    def readinto(self, b):
        b[0:3] = b'foo'
        return 3

    def readable(self):
        return True


class TestReadinto(unittest.TestCase):

    def test_readinto(self):
        b = bytearray(5)
        r = MyRawIO()
        n = r.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b'foo\x00\x00')
        n = r.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(b, b'foo\x00\x00')
        n = r.readinto(memoryview(b)[2:4])
        self.assertEqual(n, 0)
        self.assertEqual(b, b'foo\x00\x00')
        n = r.readinto(memoryview(b))
        self.assertEqual
