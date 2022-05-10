import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)
    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
            b'')
    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write,
            b'')
    def test_name(self):
        self.assertEqual(io.RawIOBase().name, None)
    def test_close(self):
        io.RawIOBase().close()
    def test_flush(self):
        io.RawIOBase().flush()
    def test_isatty(self):
        self.assertEqual(io.RawIOBase().isatty(), False)
    def test_read1(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read1,
            b'')
   
