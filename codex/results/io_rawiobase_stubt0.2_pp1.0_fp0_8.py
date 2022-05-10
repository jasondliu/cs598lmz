import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self._file = file
        self._mode = mode
        self._closefd = closefd
        self._closed = False
        self._readable = 'r' in mode
        self._writable = 'w' in mode
        self._seekable = True
        self._offset = 0
        self._size = os.fstat(file.fileno()).st_size
        self._lock = threading.Lock()
    def readable(self):
        return self._readable
    def writable(self):
        return self._writable
    def seekable(self):
        return self._seekable
    def readinto(self, b):
        with self._lock:
            self._file.seek(self._offset)
            n = self._file.readinto(b)
            self._offset += n
            return n
    def write(self, b):
        with self._lock:
            self._file.seek(self._offset)
            n = self._file.write(b)

