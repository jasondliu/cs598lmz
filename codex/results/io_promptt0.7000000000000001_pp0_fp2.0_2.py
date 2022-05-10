import io
# Test io.RawIOBase inheritance.
def test_rawiobase():

    class MissingRawIOBase(object):
        pass


# Test io.BufferedIOBase inheritance.
def test_bufferediobase():

    class MissingBufferedIOBase(object):
        pass


# Test io.TextIOBase inheritance.
def test_textiobase():

    class MissingTextIOBase(object):
        pass


class PollableTest(unittest.TestCase):
    """Test that the object supports the minimum file interface."""

    def test_read(self):
        f = io.BytesIO(b'\xe0\xf8\xeb\xef')
        p = pollable.Pollable(f)
        self.assertEqual(p.read(2), b'\xe0\xf8')
        self.assertEqual(p.read(2), b'\xeb\xef')

    def test_readall(self):
        f = io.BytesIO(b'\xe0\xf8\xeb\xef')
        p = pollable.Pollable
