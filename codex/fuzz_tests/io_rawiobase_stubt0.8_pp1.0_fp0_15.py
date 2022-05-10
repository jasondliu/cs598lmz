import io
class File(io.RawIOBase):

    def __init__(self, path, context):
        self._path = path
        self._context = context
        self._fd = None
        self._offset = 0
        self._pos = 0
        self._size = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __repr__(self):
        return "<zbox.File path=%r, fd=%r>" % (self.path, self._fd)

    @property
    def path(self):
        return self._path

    @property
    def fileno(self):
        if self._fd is None:
            self._fd = os.open(self.path, os.O_RDWR | os.O_CREAT)
        return self._fd

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return True

    def seek(self, offset, whence=os.SEEK_
