import io
class File(io.RawIOBase):
    def __init__(self, file, mode='rb', closefd=True):
        self._file = file
        self._mode = mode
        self._closefd = closefd
        self._readbuffer = b''
        self._writebuffer = b''
        self._offset = 0
        self._pos = 0
        self._size = os.fstat(self._file.fileno()).st_size

    def readinto(self, b):
        if self._pos == self._size:
            return 0
        if self._pos + len(b) > self._size:
            b = b[:self._size - self._pos]
        self._readbuffer += os.read(self._file.fileno(), len(b))
        b[:len(self._readbuffer)] = self._readbuffer
        self._readbuffer = self._readbuffer[len(b):]
        self._pos += len(b)
        return len(b)

    def write(self, b):
        if self._pos == self._size:
            return 0
        if self._pos
