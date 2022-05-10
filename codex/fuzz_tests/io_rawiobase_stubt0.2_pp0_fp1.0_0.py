import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self.close()
        self.open(name, mode, buffering, encoding, errors, newline, closefd, opener)
    def open(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        if self.fd is not None:
            self.close()
        if isinstance(name, int):
            fd = name
            if not closefd:
                self.fd = fd
                return
        else:
            if opener is not None:
                fd = opener(name, mode)
            else:
                fd
