import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.file = None
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return False
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def readable(self):
        return 'r' in self.mode
    def writable(self):
        return 'w' in self.mode
    def seekable(self):
        return False
    def read(self, size=-1):
        if not self.readable():
            raise io.UnsupportedOperation("read()")
        if self.file is None:
            self.file = open(self.name, self.mode)
        return self.file.read(size)

