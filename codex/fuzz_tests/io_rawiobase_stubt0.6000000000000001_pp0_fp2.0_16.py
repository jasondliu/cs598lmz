import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', buffering=-1,
                 encoding=None, errors=None, newline=None,
                 closefd=None, opener=None):
        self.path = path
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.f = open(self.path, self.mode)
        self.read = self.f.read
        self.readline = self.f.readline
    def close(self, *args, **kwargs):
        self.f.close()
        return self
    def flush(self, *args, **kwargs):
        return self.f.flush(*args, **kwargs)
    def fileno(self, *args, **kwargs):
        return self.f.fileno(*args, **kwargs)
    def isatty(self, *args, **kwargs):
        return self
