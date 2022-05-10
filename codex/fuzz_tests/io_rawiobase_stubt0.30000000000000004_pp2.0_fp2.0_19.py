import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.f = open(name, 'rb')
    def close(self):
        if self.f is not None:
            self.f.close()
            self.f = None
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return False
    def readable(self):
        return True
    def readinto(self, b):
        return self.f.readinto(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def writable(self):
        return False
    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.name)
    def __str__(self):
        return '<%s %r at %#x>' % (
