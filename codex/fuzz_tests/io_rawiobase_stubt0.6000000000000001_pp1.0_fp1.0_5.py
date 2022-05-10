import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.f = open(name, mode)
        self.fd = self.f.fileno()
    def read(self, n=-1):
        return self.f.read(n)
    def readinto(self, b):
        return self.f.readinto(b)
    def write(self, b):
        return self.f.write(b)
    @property
    def closed(self):
        return self.f.closed
    def close(self):
        return self.f.close()
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    def readable(self):
        return self.f.readable()
    def seekable(self):
        return self.f.seekable()
    def writable(self):
        return self.f.writable()
    def seek(self, offset, whence=0):
       
