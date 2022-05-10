import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.fd = None
        self.close()
        self.open(name, mode, buffering)
    def open(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
        if self.fd is not None:
            self.close()
        if self.mode is None:
            self.mode = mode
        if self.mode in ('r', 'w', 'x', 'a', 'r+', 'w+', 'x+', 'a+'):
            self.mode = self.mode + 'b'
        self.fd = open(name, self.mode, buffering)
        self.closefd = closefd
       
