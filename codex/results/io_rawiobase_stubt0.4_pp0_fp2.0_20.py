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
    def __del__(self):
        self.close()
    def close(self):
        if self.fd:
            self.fd.close()
            self.fd = None
    def fileno(self):
        if not self.fd:
            self.fd = open(self.name, self.mode, self.closefd, self.opener)
        return self.fd.fileno()
    def seekable(self):
        return True
    def readable(self):
        return 'r' in self.mode
    def writable(self):
        return 'w' in self.mode
    def
