import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, n, whence=io.SEEK_SET):
        return self.file.seek(n, whence)
    def tell(self):
        return self.file.tell()
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        b[:n] = data
        return n
    def close(self):
        return self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

def read_file(file):
    return File(file)
