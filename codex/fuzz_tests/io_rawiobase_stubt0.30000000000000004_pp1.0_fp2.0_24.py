import io
class File(io.RawIOBase):
    def __init__(self, filepath, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.filepath = filepath
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
            self.fd = self.opener(self.filepath, self.mode, self.buffering)
        else:
            self.fd = open(self.filepath, self.mode, self.buffering, self.encoding, self.errors, self.newline, self.closefd)
    def close(self):
        if self.fd is not None:
            self.fd.close()
            self.fd = None
    def __enter__(self):
        return
