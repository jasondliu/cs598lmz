import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.name, self.mode)
    def close(self):
        self.file.close()
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        self.file.write(b)
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        self.file.flush()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seekable(
