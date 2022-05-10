import io
class File(io.RawIOBase):
    def __init__(self, f, *args):
        self.closed = f.closed
        self.encoding = f.encoding
        self.mode = f.mode
        self.name = f.name
        self.newlines = f.newlines
        self.softspace = f.softspace
        self.file = f.file
        self.args = args

    def isatty(self):
        return self.file.isatty()
    def close(self):
        self.file.close()
        self.closed = self.file.closed
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        return self.file.flush()
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seekable(self):
        return self.file.seekable()
    def read(self, n):
        return self.file.read(n)
    def readinto(self, b):
        return self
