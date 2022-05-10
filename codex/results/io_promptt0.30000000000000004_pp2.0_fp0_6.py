import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        self.assertEqual(io.RawIOBase.read(None, 0), b'')
        self.assertRaises(TypeError, io.RawIOBase.read)

    def test_readinto(self):
        self.assertEqual(io.RawIOBase.readinto(None, b''), 0)
        self.assertRaises(TypeError, io.RawIOBase.readinto)

    def test_readall(self):
        self.assertEqual(io.RawIOBase.readall(None), b'')
        self.assertRaises(TypeError, io.RawIOBase.readall)

    def test_write(self):
        self.assertEqual(io.RawIOBase.write(None, b''), 0)
        self.assertRaises(TypeError, io.RawIOBase.write)

    def test_seek(self):
        self.assertEqual(io.RawIOBase.seek(None, 0, 0), 0)
