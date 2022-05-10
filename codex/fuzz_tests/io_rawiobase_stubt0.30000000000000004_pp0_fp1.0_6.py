import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.name = filename
        self.mode = mode
        self.fd = os.open(filename, os.O_RDONLY)
        self.length = os.fstat(self.fd).st_size
        self.pos = 0
    def close(self):
        if self.fd:
            os.close(self.fd)
            self.fd = None
    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = self.length + offset
        else:
            raise ValueError("invalid whence (%r, should be 0, 1 or 2)" % whence)
        return self.pos
    def tell(self):
        return self.pos
    def readinto(self, b):
        n = os.read(self.fd, b)
        self.pos += n
        return n
    def readable(self):

