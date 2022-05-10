import io
# Test io.RawIOBase.readinto
class RawIOBaseTest(unittest.TestCase):

    def test_readinto(self):
        rio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rio.readinto, b'')
        self.assertRaises(io.UnsupportedOperation, rio.readinto, bytearray())


class BytesIO(io.BytesIO):
    """Bytes IO that supports readinto()."""

    def readinto(self, b):
        data = self.read(len(b))
        n = len(data)
        b[:n] = data
        return n


def bytearray_write_only():
    b = bytearray(b'test')
    return io.BytesIO(b)


def bytearray_read_write():
    b = bytearray(b'test')
    return BytesIO(b)


def bytes_write_only():
    return io.BytesIO(b'test')


def bytes_read_write():
    return
