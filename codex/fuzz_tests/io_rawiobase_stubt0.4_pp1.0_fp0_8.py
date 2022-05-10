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
        self.file = self.opener(self.path, self.mode, self.buffering)
        self.readable = self.writable = self.seekable = False
        if 'r' in self.mode:
            self.readable = True
        if 'w' in self.mode:
            self.writable = True
        if '+' in self.mode:
            self.readable = self.writable = True
        if self.readable:
            self.seekable = True
        self.closed = False
    def close(self):
        if self.closed:
            raise ValueError('I/O operation on closed file
