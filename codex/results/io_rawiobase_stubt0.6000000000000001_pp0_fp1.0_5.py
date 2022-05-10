import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.f = open(name, 'rb')
    def close(self):
        if self.f:
            self.f.close()
        self.f = None
    def seekable(self):
        return True
    def readable(self):
        return True
    def seek(self, pos, whence=0):
        self.f.seek(pos, whence)
    def tell(self):
        return self.f.tell()
    def readinto(self, buf):
        return self.f.readinto(buf)
    def read(self, size=-1):
        return self.f.read(size)
    def readall(self):
        return self.f.readall()

def open(name, mode='r'):
    if 'b' in mode:
        return File(name)
    else:
        return io.TextIOWrapper(File(name), encoding='utf-8')
