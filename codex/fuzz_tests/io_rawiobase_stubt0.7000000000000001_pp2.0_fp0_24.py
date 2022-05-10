import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.file = open(path, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def read1(self, size=-1):
        return self.file.read1(size)
    def readinto(self, b):
        return self.file.readinto(b)
    def writable(self):
        return self.mode in ('w', 'a', 'x', 'w+', 'a+', 'x+')
    def write(self, b):
        return self.file.write(b)
    def flush(self):
        return self.file.flush()
    def readable(self):
        return self.mode in ('r', 'r+', 'w+', 'a+', 'x+')
    def seek(self, pos, whence=0):
        return self.file.seek(pos, whence)
    def seekable(self):
        return True
    def
