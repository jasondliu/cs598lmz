import io
class File(io.RawIOBase):
    def write(self, b):
        return len(b)

class TestFileIO(unittest.TestCase):
    def test_closefd(self):
        f = File()
        f.closefd()
        with self.assertRaises(ValueError):
            f.write(b'')

    def test_closefd_closed(self):
        f = File()
        f.close()
        f.closefd()
        with self.assertRaises(ValueError):
            f.write(b'')


class TestRawIOBase(unittest.TestCase):
    def test_readall(self):
        with io.BytesIO(b'foo') as f:
            self.assertEqual(f.readall(), b'foo')

    def test_readinto(self):
        with io.BytesIO(b'foo') as f:
            b = bytearray(4)
            self.assertEqual(f.readinto(b), 3)
            self.assertEqual(b, b'foo\x00')

    def
