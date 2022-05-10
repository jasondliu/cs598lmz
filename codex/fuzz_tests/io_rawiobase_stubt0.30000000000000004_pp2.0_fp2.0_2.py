import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        return self.file.write(b)
    def readinto(self, b):
        return self.file.readinto(b)
    def truncate(self, size=None):
        return self.file.truncate(size)
    def flush(self):
        return self.file.flush()
    def close(self):
        return self.file.close()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
   
