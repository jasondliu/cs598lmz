import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.f = io.open(filename, 'rb')
    def read(self, size=-1):
        return self.f.read(size)
    def tell(self):
        return self.f.tell()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def close(self):
        return self.f.close()

# Python 2.6
class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, 'rb')
    def read(self, size=-1):
        return self.f.read(size)
    def tell(self):
        return self.f.tell()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def close(self):
        return self.f.close()

# Python 2.5
class File(object):
    def __init__
