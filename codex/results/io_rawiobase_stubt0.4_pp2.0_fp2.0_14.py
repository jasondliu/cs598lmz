import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self._mode = mode
        self._name = name
        self._file = open(name, mode)
        self._size = os.stat(name).st_size

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._file.close()

    def fileno(self):
        return self._file.fileno()

    def flush(self):
        self._file.flush()

    def isatty(self):
        return self._file.isatty()

    def readable(self):
        return self._mode == 'r'

    def readinto(self, b):
        return self._file.readinto(b)

    def readline(self, limit=-1):
        return self._file.readline(limit)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence ==
