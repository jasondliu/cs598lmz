import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.mode = mode
        self.f = open(filename, mode + 'b')
    def close(self):
        if self.f:
            self.f.close()
            self.f = None
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
    def readable(self):
        return 'r' in self.mode
    def writable(self):
        return 'w' in self.mode
    def seekable(self):
        return True
    def readinto(self, b):
        return self.f.readinto(b)
    def write(self, b):
        return self.f.write(b)
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def flush(self):
        return self.f.flush()
    def fileno(self):
        return
