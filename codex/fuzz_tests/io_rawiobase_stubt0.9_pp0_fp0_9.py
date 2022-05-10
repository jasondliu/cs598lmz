import io
class File(io.RawIOBase):
    __qualname__ = 'File'

    def __init__(self, file):
        self._file = file
        self._progress = 0
        self._start = 0
        self._size = None

    def read(self, size=None):
        if size is None:
            size = self.size - self.progress
        data = self._file.read(size)
        self._progress += len(data)
        return data

    def tell(self):
        return self._file.tell()

    def seek(self, offset, whence=io.SEEK_SET):
        if not self._size:
            self._size = self._file.size
        self._start = self._file.seek(offset, whence)
        self._progress = 0
        return self._start

    @property
    def progress(self):
        return self._progress + self._start

    @property
    def size(self):
        if self._size is None:
            return self._file.size
        return self._size
if __name__ == '__main__':
    with open
