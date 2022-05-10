import io
# Test io.RawIOBase.readinto()

class RawIOBaseSubclass(io.RawIOBase):
    def __init__(self, len):
        self.len = len
        self.pos = 0

    def readinto(self, b):
        if self.pos >= self.len:
            return None
        n = min(len(b), self.len - self.pos)
        b[:n] = list(range(self.pos, self.pos + n))
        self.pos += n
        return n

    def readable(self):
        return True

class TestRawIOBaseReadinto(unittest.TestCase):
    def test_readinto(self):
        buf = bytearray(10)
        with RawIOBaseSubclass(10) as f:
            self.assertEqual(f.readinto(buf), 10)
            self.assertEqual(buf, bytearray(list(range(10))))
            self.assertEqual(f.readinto(buf), None)
            self.assertEqual(buf, bytearray(list(
