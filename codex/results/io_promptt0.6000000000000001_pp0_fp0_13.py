import io
# Test io.RawIOBase.
assert issubclass(io.RawIOBase, io.IOBase)
assert issubclass(io.RawIOBase, object)

class BaseTestRawIO(BaseTestIO):

    def test_readall(self):
        self.assertEqual(self.io.readall(), self.data[:self.size])

    def test_readinto(self):
        b = bytearray(5)
        self.io.readinto(b)
        self.assertEqual(bytes(b), self.data[:5])

    def test_readinto_resize(self):
        b = bytearray(1)
        n = self.io.readinto(b)
        self.assertEqual(n, 1)
        self.assertEqual(len(b), 1)
        n = self.io.readinto(b)
        self.assertEqual(n, 1)
        self.assertEqual(len(b), 2)
        n = self.io.readinto(b)
        self.assertEqual(n, 1
