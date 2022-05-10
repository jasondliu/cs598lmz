import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test___init__(self):
        r = io.RawIOBase()

    def test_close(self):
        r = io.RawIOBase()
        r.close()

    def test_closed(self):
        r = io.RawIOBase()
        self.assertRaises(NotImplementedError, r.closed)

    def test_fileno(self):
        r = io.RawIOBase()
        self.assertRaises(NotImplementedError, r.fileno)

    def test_flush(self):
        r = io.RawIOBase()
        r.flush()

    def test_isatty(self):
        r = io.RawIOBase()
        self.assertRaises(NotImplementedError, r.isatty)

    def test_read(self):
        r = io.RawIOBase()
        self.assertRaises(NotImplementedError, r.read)

    def test_readable(self):
        r = io.RawIO
