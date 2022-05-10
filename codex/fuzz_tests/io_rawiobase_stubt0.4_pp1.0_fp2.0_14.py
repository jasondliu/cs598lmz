import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def fileno(self):
        return self.f.fileno()
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.f.seek(offset)
        elif whence == io.SEEK_CUR:
            self.f.seek(self.f.tell() + offset)
        elif whence == io.SEEK_END:
            self.f.seek(self.f.seek(0, 2) + offset)
        else:
            raise ValueError('Invalid value for whence.')
        return self.f.tell()
    def tell(self):
        return self.f.tell()
    def flush(self):
        return self.f.
