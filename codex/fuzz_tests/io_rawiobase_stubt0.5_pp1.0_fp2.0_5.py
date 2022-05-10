import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 0:
            self.f.seek(offset)
        elif whence == 1:
            self.f.seek(self.f.tell() + offset)
        elif whence == 2:
            self.f.seek(self.f.seek(0, 2) + offset)
        return self.f.tell()
    def tell(self):
        return self.f.tell()
    def readable(self):
        return True
    def writable(self):
        return False
    def flush(self):
        pass

class BytesIO(io.BytesIO):
    def __init__(self, buf=b''):
        super().__init__(buf)
    def seekable(self):
        return True
    def readable(self):
        return True
    def
