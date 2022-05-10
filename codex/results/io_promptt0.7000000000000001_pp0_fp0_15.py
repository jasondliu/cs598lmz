import io
# Test io.RawIOBase.readinto()

class BaseTestRawIO(object):
    def test_readinto(self):
        rawio = self.RawIO(b"abc")
        b = bytearray(2)
        n = rawio.readinto(b)
        self.assertEqual(n, 2)
        self.assertEqual(b, b"ab")
        n = rawio.readinto(b)
        self.assertEqual(n, 1)
        self.assertEqual(b, b"c\x00")
        n = rawio.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(b, b"c\x00")

    def test_readinto_resize(self):
        rawio = self.RawIO(b"abc")
        b = bytearray(1)
        n = rawio.readinto(b)
        self.assertEqual(n, 1)
        self.assertEqual(b, b"a")
        # result of readinto() should not
