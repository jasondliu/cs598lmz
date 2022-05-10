import io
class File(io.RawIOBase):
    """
    A file-like object that reads from a string buffer.
    """
    def __init__(self, buffer=b'', name=None):
        self._buffer = buffer
        self._name = name
        self._offset = 0

    def readable(self):
        return True

    def readinto(self, b):
        n = len(b)
        if self._offset + n > len(self._buffer):
            n = len(self._buffer) - self._offset
        b[:n] = self._buffer[self._offset:self._offset + n]
        self._offset += n
        return n

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self._offset = offset
        elif whence == 1:
            self._offset += offset
        elif whence == 2:
            self._offset = len(self._buffer) + offset
        return self._offset

    def tell(self):
        return self._offset

    def writable(self):
        return
