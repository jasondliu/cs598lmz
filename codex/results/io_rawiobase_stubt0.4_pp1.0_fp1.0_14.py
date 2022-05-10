import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self._path = path
        self._mode = mode
        self._file = None
        self._pos = 0
        self._size = 0
        self._lock = threading.Lock()

    def readinto(self, b):
        with self._lock:
            if self._file is None:
                self._file = open(self._path, self._mode)
                self._size = os.fstat(self._file.fileno()).st_size
            if self._pos >= self._size:
                return 0
            n = self._file.readinto(b)
            self._pos += n
            return n

    def seek(self, pos, whence=0):
        with self._lock:
            if self._file is None:
                self._file = open(self._path, self._mode)
                self._size = os.fstat(self._file.fileno()).st_size
            if whence == 0:
                new_pos = pos
            elif whence == 1:
               
