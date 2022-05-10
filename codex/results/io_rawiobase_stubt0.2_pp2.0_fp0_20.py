import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._offset = 0
        self._size = os.fstat(file.fileno()).st_size
    def readinto(self, b):
        if not self._reading:
            raise OSError(errno.EBADF, 'File not open for reading')
        l = len(b)
        if self._offset >= self._size:
            return None
        if self._offset + l > self._size:
            l = self._size - self._offset
        os.lseek(self._file.fileno(), self._offset, os.SEEK_SET)
        n = os.read(self._file.fileno(), b[:l])
        self._offset += n
        return n
    def write(self, b):
        if not self._writing:
            raise OSError(errno.EBADF, 'File
