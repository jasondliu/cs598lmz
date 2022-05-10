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
        self.close()
        self.open(path, mode, buffering, encoding, errors, newline, closefd, opener)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def __del__(self):
        self.close()
    def __repr__(self):
        return '<File %r>' % self.path
    def open(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, close
