import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.filename, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def readline(self, size=-1):
        return self.file.readline(size)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        return self.file.write(b)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class File2(io.RawIOBase):
    def __init__(self, filename, mode='r
