import io
class File(io.RawIOBase):
    def __init__(self, name, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.close()
        self.open(name, mode, buffering, encoding, errors, newline, closefd, opener)
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def __del__(self):
        self.close()
    def open(self, name, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        if self.file is not None:
            self.close()
        if not isinstance(name, str):
            raise TypeError("invalid file: %r" %
