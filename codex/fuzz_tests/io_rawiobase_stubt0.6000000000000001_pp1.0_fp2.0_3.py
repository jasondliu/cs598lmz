import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self._filename = filename
        self._mode = mode
        self._file = None
        self._pos = 0
        if self._mode == 'r':
            self._file = open(self._filename, 'rb')
        else:
            raise NotImplementedError
    def read(self, size=-1):
        if self._file is None:
            raise ValueError('I/O operation on closed file')
        if size < 0:
            size = self.size - self._pos
        self._file.seek(self._pos)
        data = self._file.read(size)
        self._pos += len(data)
        return data
    def seek(self, offset, whence=io.SEEK_SET):
        if self._file is None:
            raise ValueError('I/O operation on closed file')
        if whence == io.SEEK_SET:
            self._pos = offset
        elif whence == io.SEEK_CUR:
            self._pos += offset
        elif
