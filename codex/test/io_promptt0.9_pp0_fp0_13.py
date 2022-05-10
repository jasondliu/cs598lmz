import io
# Test io.RawIOBase.readall()


class RawBytes(io.RawIOBase):

    def __init__(self):
        self._data = b'abcdefghijklmnopqrstuvwxyz'
        self._pos = 0

    def readall(self):
        return self.read()

    def read(self, size=None):
        if size is None:
            size = len(self._data)
        else:
            size = min(size, len(self._data) - self._pos)
        rv = self._data[self._pos:self._pos+size]
        self._pos += size
        return rv

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            new_pos = offset
        elif whence == 1:
            new_pos = self._pos + offset
        elif whence == 2:
            new_pos = len(self._data) + offset
