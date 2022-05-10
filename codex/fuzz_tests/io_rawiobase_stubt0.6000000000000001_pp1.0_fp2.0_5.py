import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.buf = b''
    def readable(self):
        return True
    def readinto(self, b):
        l = len(b) # space available in b
        chunk = self.f.read(l)
        n = len(chunk)
        self.buf = chunk[n:] # save the extra
        b[:n] = chunk[:n] # copy the bytes into b
        return n
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 1:
            offset = self.f.tell() + len(self.buf) + offset
        self.buf = b''
        self.f.seek(offset, 0)
        return self.f.tell()
    def tell(self):
        return self.f.tell() + len(self.buf)
    def writable(self):
        return True
    def write(self, b):
        self.buf = b
        return len(b)
