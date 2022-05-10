import io
class File(io.RawIOBase):
    """
    A file-like object that reads from a file descriptor.
    """
    def __init__(self, fd, mode='r'):
        self._fd = fd
        self._mode = mode
        self._pos = 0
        self._closed = False

    def __repr__(self):
        return '<File {}>'.format(self._fd)

    def close(self):
        if not self._closed:
            os.close(self._fd)
            self._closed = True

    def fileno(self):
        return self._fd

    def readable(self):
        return 'r' in self._mode

    def writable(self):
        return 'w' in self._mode

    def seekable(self):
        return False

    def read(self, size=-1):
        if not self.readable():
            raise io.UnsupportedOperation()
        if size < 0:
            size = os.SEEK_END
        return os.read(self._fd, size)

    def write(self, b):
        if not self
