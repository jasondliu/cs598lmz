import io
class File(io.RawIOBase):
    """A class that provides a file-like interface on top of a byte array."""

    def __init__(self, data, file_name=None):
        self._data = data
        self._file_name = file_name
        self._pos = 0

    def __repr__(self):
        if self._file_name is None:
            return '<ByteArrayFile len=%d>' % len(self._data)
        else:
            return '<ByteArrayFile %r len=%d>' % (self._file_name, len(self._data))

    def __len__(self):
        return len(self._data)

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def read(self, length=-1):
        if length < 0:
            length = len(self._data) - self._pos
        if length < 0:
            return b''
        r = self._data[self._pos:self._pos + length]
        self
