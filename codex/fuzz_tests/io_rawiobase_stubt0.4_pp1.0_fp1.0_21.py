import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.f = open(filename, mode)
        self.f.seek(0, 2)
        self.size = self.f.tell()
        self.f.seek(0)
    def read(self, size=-1):
        return self.f.read(size)
    def tell(self):
        return self.f.tell()
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)
    def close(self):
        self.f.close()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class FileReader(io.RawIOBase):
    def __init__(self, filename):
        self.f = open(filename, 'rb')
        self.f.seek(0, 2)
        self.size = self.f.tell()
        self.f.seek(0)
    def read(self, size
