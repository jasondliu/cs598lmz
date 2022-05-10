import io
class File(io.RawIOBase):
    def __init__(self, stor):
        self._stor = stor
        self._pos = 0
        self._size = self._stor.size
    def read(self, size=-1):
        if not self._stor:
            return
        pos = self._pos
        self._pos += size
        if self._pos > self._size:
            size -= self._pos - self._size
            self._pos = self._size
        return self._stor.read(pos, size)
    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self._pos = pos
        elif whence == io.SEEK_CUR:
            self._pos += pos
        elif whence == io.SEEK_END:
            self._pos = self._size + pos
    def tell(self):
        return self._pos
    def close(self):
        self._stor = None
    def readable(self):
        return True
    def writable(self):
        return False

