import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        if mode not in ('r', 'w'):
            raise ValueError("invalid mode: %r" % (mode,))
        self._mode = mode
        self._path = path
        self._pos = 0
        self._fd = None
        self._buf = ""

    @property
    def name(self):
        return self._path

    @property
    def mode(self):
        return self._mode

    def close(self):
        self._buf = None
        if self._fd is not None:
            os.close(self._fd)
            self._fd = None

    def closed(self):
        return self._fd is None

    def fileno(self):
        if self._fd is None:
            self._fd = os.open(self._path, os.O_RDWR)
        return self._fd

    def seekable(self):
        return True

    def readable(self):
        return self._mode == 'r'

    def writable(self):
        return
