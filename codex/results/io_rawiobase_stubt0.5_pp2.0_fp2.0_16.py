import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.handle = open(name, mode)
        self.mode = mode
        self.name = name
    def read(self, n=-1):
        return self.handle.read(n)
    def write(self, b):
        return self.handle.write(b)
    def fileno(self):
        return self.handle.fileno()
    def seekable(self):
        return self.handle.seekable()
    def readable(self):
        return self.mode in ('r', 'r+', 'a+')
    def writable(self):
        return self.mode in ('w', 'a', 'r+', 'a+')
    def seek(self, offset, whence=0):
        return self.handle.seek(offset, whence)
    def tell(self):
        return self.handle.tell()
    def truncate(self, size=None):
        return self.handle.truncate(size)
    def flush(self):
        return self.handle.flush()
   
