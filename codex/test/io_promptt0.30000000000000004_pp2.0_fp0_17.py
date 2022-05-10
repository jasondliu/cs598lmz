import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self, raw):
        self.raw = raw
    def read(self, n=-1):
        return self.raw.read(n)
    def write(self, b):
        return self.raw.write(b)
    def fileno(self):
        return self.raw.fileno()
    def seekable(self):
        return self.raw.seekable()
    def readable(self):
        return self.raw.readable()
    def writable(self):
        return self.raw.writable()
    def seek(self, pos, whence=0):
        return self.raw.seek(pos, whence)
    def tell(self):
        return self.raw.tell()
    def truncate(self, pos=None):
        return self.raw.truncate(pos)
    def close(self):
        return self.raw.close()
    def flush(self):
        return self.raw.flush()
    def readinto(self, b):
        return self
