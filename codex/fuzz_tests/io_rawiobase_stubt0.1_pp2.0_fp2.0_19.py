import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._closed = False
        self._pos = 0
        self._size = 0
        if self._writing:
            self._size = len(file)
    def readinto(self, b):
        if not self._reading:
            raise io.UnsupportedOperation("File was not opened for reading")
        if self._closed:
            raise ValueError("I/O operation on closed file")
        if self._pos >= self._size:
            return 0
        n = min(len(b), self._size - self._pos)
        b[:n] = self._file[self._pos:self._pos+n]
        self._pos += n
        return n
    def write(self, b):
        if not self._writing:
            raise io.UnsupportedOperation("File was not opened for writing")
        if self._closed:
            raise ValueError
