import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
    def fileno(self):
        return self.f.fileno()
    def seekable(self):
        return self.f.seekable()
    def seek(self, offset, whence=io.SEEK_SET):
        self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def truncate(self, size=None):
        return self.f.truncate(size)
    def flush(self):
        self.f.flush()
    def close(self):
        self.f.close()

from io import BytesIO
class File(BytesIO):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(
