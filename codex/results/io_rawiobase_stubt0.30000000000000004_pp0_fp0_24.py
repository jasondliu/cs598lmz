import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.f = open(path, 'rb')
        self.size = os.fstat(self.f.fileno()).st_size
    def read(self, n):
        return self.f.read(n)
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def __len__(self):
        return self.size
    def close(self):
        return self.f.close()

class FileReader(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.f = open(path, 'rb')
        self.size = os.fstat(self.f.fileno()).st_size
    def read(self, n):
        return self.f.read(n)
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence
