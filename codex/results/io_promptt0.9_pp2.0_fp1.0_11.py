import io
# Test io.RawIOBase subclass with custom fileno() method
class FNoRawIO(io.RawIOBase):

    def __init__(self, fileno=-2):
        self._fileno = fileno

    def fileno(self):
        return self._fileno

with self.assertRaises(ValueError):
    FNoRawIO().read(1)


class FNoRawIO2(io.RawIOBase):

    def __init__(self, fileno=-2):
        self._fileno = fileno

    @property
    def fileno(self):
        return self._fileno

with self.assertRaises(ValueError):
    FNoRawIO2().read(1)


# Test io.RawIOBase subclass with custom readinto() method
class RIOReadinto(io.RawIOBase):

    def readinto(self, b):
        data = bytearray(b"foobar", 'latin-1')
        b[:len(data)] = data
        return len(data)


with self.assertRaises(io.UnsupportedOperation):

