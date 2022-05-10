import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None
    def open(self):
        self.file = open(self.name, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        return self.file.flush()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return self.file.readable()
    def readline(self, size=-1):
        return self.file.readline(size)

