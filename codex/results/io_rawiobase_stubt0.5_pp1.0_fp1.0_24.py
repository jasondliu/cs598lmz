import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.seekable = f.seekable()
        self.readable = f.readable()
        self.writable = f.writable()
        self.closed = f.closed
        self.mode = f.mode
        self.name = f.name
        self.newlines = f.newlines

    def read(self, size=-1):
        return self.f.read(size)

    def readinto(self, b):
        return self.f.readinto(b)

    def read1(self, size=-1):
        return self.f.read1(size)

    def write(self, b):
        return self.f.write(b)

    def seek(self, pos, whence=0):
        return self.f.seek(pos, whence)

    def tell(self):
        return self.f.tell()

    def truncate(self, size=None):
        return self.f.truncate(size)

    def flush(self):
        return self
