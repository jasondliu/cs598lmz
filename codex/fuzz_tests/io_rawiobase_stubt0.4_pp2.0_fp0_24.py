import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        self.file.close()

class Zip(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.pos = 0
    def read(self, n=-1):
        if n < 0:
            n = self.file.size - self.pos
        self.pos += n
        return self.file.read(n)
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = offset
        elif whence == io.SEEK_CUR:
            self.pos += offset
        elif whence == io.SEEK_END
