import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
    def seek(self, n, whence=0):
        self.f.seek(n, whence)
    def tell(self):
        return self.f.tell()

class ZipFile(File):
    def __init__(self, f):
        super().__init__(f)
    def read(self, n=-1):
        return super().read(n).decode("utf-8")
    def write(self, b):
        super().write(b.encode("utf-8"))

class GzipFile(File):
    def __init__(self, f):
        super().__init__(f)
    def read(self, n=-1):
        return super().read(n).decode("utf-8")
    def write(self, b):
        super().write(b.encode
