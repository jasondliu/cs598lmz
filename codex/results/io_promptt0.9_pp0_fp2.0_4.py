import io
# Test io.RawIOBase with one of its convenient subclasses
class Subclass(io.BufferedIOBase):
    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def close(self):
        pass

    def flush(self):
        pass

    def read(self, n = -1):
        return b'foo'

    def read1(self, n = -1):
        return b'bar'

    def seek(self, offset, whence=io.SEEK_SET):
        pass

    def tell(self):
        return 1
# now test io.RawIOBase itself


def read_size(size):
    return b'x' * size


class ReadMixin(object):
    # RawIOBase has separate reads and read1 methods.
    # This mixin class is used to run the same tests for both.
    def test_readinto(self):
        b = bytearray(10)
        n = self.io.readinto(b)
        self.assertEqual(
