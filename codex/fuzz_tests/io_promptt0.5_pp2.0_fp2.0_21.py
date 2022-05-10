import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        with self.assertRaises(io.UnsupportedOperation) as cm:
            io.RawIOBase().read(1)
        self.assertEqual(str(cm.exception), "read() not supported")

    def test_readinto(self):
        with self.assertRaises(io.UnsupportedOperation) as cm:
            io.RawIOBase().readinto(bytearray(1))
        self.assertEqual(str(cm.exception), "readinto() not supported")

    def test_write(self):
        with self.assertRaises(io.UnsupportedOperation) as cm:
            io.RawIOBase().write(b"")
        self.assertEqual(str(cm.exception), "write() not supported")

    def test_seek(self):
        with self.assertRaises(io.UnsupportedOperation) as cm:
            io.RawIOBase().seek(0)
        self.assertEqual(str(cm.ex
