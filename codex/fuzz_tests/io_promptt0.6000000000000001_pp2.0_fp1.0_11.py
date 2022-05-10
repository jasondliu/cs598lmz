import io
# Test io.RawIOBase.read() with a large buffer size

class TestRawIO(io.RawIOBase):
    def __init__(self, data):
        self._data = data
        self._pos = 0

    def read(self, size=-1):
        if size < 0:
            size = len(self._data) - self._pos
        elif size > len(self._data) - self._pos:
            size = len(self._data) - self._pos
        r = self._data[self._pos:self._pos + size]
        self._pos += size
        return r

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            newpos = pos
        elif whence == 1:
            newpos = self._pos + pos
        elif whence == 2:
            newpos = len(self._data) + pos
        else:
            raise ValueError("whence must be 0, 1 or 2, not {!r}".format(whence))
        if newpos < 0:

