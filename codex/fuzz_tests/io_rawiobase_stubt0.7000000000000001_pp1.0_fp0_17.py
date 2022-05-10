import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def __del__(self):
        self.close()
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return True
    def readinto(self, b):
        ret = self.file.readinto(b)
        return ret
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def seek(self, pos, whence=io.SEEK_SET):
        return self.file.seek(pos, whence)
    def tell(self):
        return self.file.tell()
    def truncate(self, pos=None):
        return self.file.truncate(pos)
    def flush(self):

