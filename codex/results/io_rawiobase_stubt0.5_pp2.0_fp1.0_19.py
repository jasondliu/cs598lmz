import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        super().__init__()
        self.name = name
        self.mode = mode
        self.file = None
        self._open()
    def _open(self):
        self.file = open(self.name, self.mode)
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readable(self):
        return self.mode in ('r', 'r+', 'a+')
    def writable(self):
        return self.mode in ('w', 'r+', 'a+', 'a')
    def seekable(self):
        return self.file.seekable()
    def readinto(self, b):
        return self.file.readinto(b)
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def tell(self):
        return self.file.tell()
