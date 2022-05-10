import io
# Test io.RawIOBase
class RawIOBaseSubclass(io.RawIOBase):
    def __init__(self, value):
        self.value = value
    def read(self, n=-1):
        return self.value
    def write(self, b):
        self.value = b
    def close(self):
        pass

class TestRawIOBase(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)
    def test_read(self):
        r = RawIOBaseSubclass(b"abc")
        self.assertEqual(r.read(2), b"ab")
        self.assertEqual(r.read(2), b"c")
        self.assertEqual(r.read(2), b"")
        self.assertEqual(r.read(2), b"")
        r = RawIOBaseSubclass(b"abc")
        self.assertEqual(r.read(), b"abc")
        self.assertEqual(r.read(), b"")
