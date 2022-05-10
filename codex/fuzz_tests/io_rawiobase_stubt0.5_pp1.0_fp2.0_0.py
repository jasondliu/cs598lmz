import io
class File(io.RawIOBase):
    def read(self, size = -1):
        return b'\x00' * size

class TestFile(unittest.TestCase):
    def test_read(self):
        f = File()
        self.assertEqual(f.read(0), b'')
        self.assertEqual(f.read(1), b'\x00')
        self.assertEqual(f.read(10), b'\x00' * 10)
        self.assertEqual(f.read(100), b'\x00' * 100)
        self.assertEqual(f.read(), b'')
        f = File()
        self.assertEqual(f.read(-1), b'\x00' * (2 ** 31 - 1))
        self.assertEqual(f.read(-1), b'')
        f = File()
        self.assertEqual(f.read(None), b'')
        f = File()
        self.assertEqual(f.read(2 ** 31), b'')
        f = File()
       
