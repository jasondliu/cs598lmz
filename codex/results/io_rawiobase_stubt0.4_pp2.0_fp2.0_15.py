import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._path = path
        self._file = None
        self._pos = 0
        self._size = os.path.getsize(self._path)
    def read(self, size=-1):
        if self._file is None:
            self._file = open(self._path, 'rb')
        if size < 0:
            size = self._size - self._pos
        data = self._file.read(size)
        self._pos += len(data)
        return data
    def seek(self, offset, whence=io.SEEK_SET):
        if self._file is None:
            self._file = open(self._path, 'rb')
        if whence == io.SEEK_SET:
            self._pos = offset
        elif whence == io.SEEK_CUR:
            self._pos += offset
        elif whence == io.SEEK_END:
            self._pos = self._size + offset
        else:
            raise ValueError('Invalid value for whence: {}'.format(whence))
