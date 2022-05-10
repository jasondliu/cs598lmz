import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'\x00'*n
    def readable(self):
        return True

class Test(unittest.TestCase):
    def test_read(self):
        f = File()
        self.assertEqual(f.read(10), b'\x00'*10)
        self.assertEqual(f.read(10), b'\x00'*10)
        self.assertEqual(f.read(10), b'\x00'*10)
        self.assertEqual(f.read(10), b'\x00'*10)
        self.assertEqual(f.read(10), b'\x00'*10)
        self.assertEqual(f.read(10), b'\x00'*10)
        self.assertEqual(f.read(10), b'\x00'*10)
        self.assertEqual(f.read(10), b'\x00'*10)
        self.assertEqual(f.read(
