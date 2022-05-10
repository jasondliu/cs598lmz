import io
class File(io.RawIOBase):
    """A simple wrapper around the open(2) system call."""

    def __init__(self, filename, mode="rb"):
        super().__init__()
        self.filename = filename
        self.mode = mode
        self._file = None
        self.newlines = None
        self.opened = False
        self.closefd = True

        try:
            self._file = os.open(filename, os.O_RDONLY)
            self.opened = True
        except OSError as e:
            if e.errno not in (errno.ENOENT, errno.EISDIR):
                raise
            # FileNotFoundError is not available on Windows
            raise FileNotFoundError(errno.ENOENT, "No such file", filename)

        self.closefd = True

    def close(self):
        if self.closed:
            return
        self.flush()
        if self.closefd:
            os.close(self._file)
        self._file = None
        self.opened = False
        self.closed = True
