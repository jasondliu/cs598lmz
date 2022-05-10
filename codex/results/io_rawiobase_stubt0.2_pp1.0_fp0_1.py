import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.path = path
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self.__open()
    def __open(self):
        if self.opener is not None:
            self.fd = self.opener(self.path, self.mode, self.closefd)
        else:
            self.fd = os.open(self.path, self.mode, self.buffering)
    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
    def __del__(self):
        self.close()
    def __enter__(self):
        return self
    def __
