import io
# Test io.RawIOBase.readinto()

import _io

try:
    _io.BytesIO
except AttributeError:
    import io
    _io = io

class TestRawIO(unittest.TestCase):
    def test_readinto(self):
        r = _io.BytesIO(b"123")
        b = bytearray(2)
        n = r.readinto(b)
        self.assertEqual(n, 2)
        self.assertEqual(b, b"12")
        n = r.readinto(b)
        self.assertEqual(n, 1)
        self.assertEqual(b[:1], b"3")
        n = r.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(b[:1], b"3")

        r = _io.BytesIO(b"123")
        b = bytearray(4)
        n = r.readinto(b)
        self.assertEqual(n, 3)
        self.assert
