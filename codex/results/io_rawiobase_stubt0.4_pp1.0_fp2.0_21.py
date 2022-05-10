import io
class File(io.RawIOBase):
    def __init__(self, name, mode, buffering=0, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closed = False
        self.close()
        self.open(name, mode, buffering, encoding, errors, newline, closefd, opener)
    def open(self, name, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        if not isinstance(name, str):
            raise TypeError("invalid file: %r" % name)
        if not isinstance(mode, str):
            raise TypeError("invalid mode: %r" % mode)
        if not isinstance(buff
