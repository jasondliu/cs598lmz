import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.seekable = True
    def readinto(self, b):
        n = self.f.readinto(b)
        if n is None:
            n = len(b)
        return n
    def readable(self):
        return True
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def writable(self):
        return False
    def write(self, b):
        raise io.UnsupportedOperation

class Socket(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
        self.seekable = False
    def readinto(self, b):
        n = self.fd.recv_into(b)
        if n is None:
            n = len(b)
        return n
    def readable(self):
        return True
    def seek(self, offset, whence=0
