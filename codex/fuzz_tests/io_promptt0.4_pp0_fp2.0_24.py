import io
# Test io.RawIOBase
try:
    io.RawIOBase
except:
    pass
else:
    class TestRawIOBase(unittest.TestCase):

        def test_read(self):
            self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

        def test_readinto(self):
            self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                              bytearray())

        def test_write(self):
            self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write,
                              b"")

        def test_close(self):
            io.RawIOBase().close()

        def test_flush(self):
            io.RawIOBase().flush()

        def test_fileno(self):
            self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)

        def test_isatty(self):
            self.assertRaises(io.UnsupportedOperation, io.RawIOBase().isatty)

        def test_seek
