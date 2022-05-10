import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None
    def open(self):
        self.file = open(self.file_name, self.mode)
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def seek(self, offset, whence=0):
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
    def writable(self):
