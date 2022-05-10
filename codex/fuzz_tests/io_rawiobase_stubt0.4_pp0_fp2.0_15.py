import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self.readable = False
        self.writable = False
        self.seekable = False
        self._open()
        self._check_mode()

    def _open(self):
        if self.opener is not None:
            self.fd = self.opener(self.path, self.mode, self.closefd)
        else:
            self.fd = open(self.path, self.mode, self.closefd)

    def _check_mode(self):
        if self.mode == 'r':
            self.readable = True
        elif self.mode == 'w':
            self.writable = True

