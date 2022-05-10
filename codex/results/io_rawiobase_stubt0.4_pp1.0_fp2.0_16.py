import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = path
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newlines = newline
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self.close()
    def close(self):
        if self.fd is not None:
            self.fd.close()
            self.fd = None
    def fileno(self):
        return self.fd.fileno()
    def flush(self):
        pass
    def isatty(self):
        return False
    def readable(self):
        return 'r' in self.mode
    def readline(self, size=-1):
        return self.fd.readline(size)
    def readlines(self, hint=-1):
        return self.fd.readlines(hint)
    def seek(self,
