import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None
    def open(self):
        self.file = open(self.path, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def readable(self):
        return self.mode.startswith('r')
    def writable(self):
        return self.mode.startswith('w')
    def seekable(self):
        return True
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
