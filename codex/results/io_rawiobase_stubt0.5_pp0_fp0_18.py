import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()

def wrap(f):
    return File(f)

class FileWrapper:
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()

def wrap(f):
    return FileWrapper(f)

class FileWrapper:
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def seek(self, offset
