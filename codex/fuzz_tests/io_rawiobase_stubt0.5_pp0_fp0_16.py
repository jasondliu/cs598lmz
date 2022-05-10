import io
class File(io.RawIOBase):
    def __init__(self, path, name, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.path = path
        self.name = name
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.path, self.mode, self.buffering, self.encoding, self.errors, self.newline, self.closefd, self.opener)
    def close(self):
        self.file.close()
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seekable(self):
        return self.file.seekable()
    def readinto(self, b
