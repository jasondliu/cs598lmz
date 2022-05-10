import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.f = open(name, 'rb')

    def read(self, n=-1):
        return self.f.read(n)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()

    def close(self):
        return self.f.close()

class File2(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.f = open(name, 'rb')

    def read(self, n=-1):
        return self.f.read(n)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)

    def tell(self):

