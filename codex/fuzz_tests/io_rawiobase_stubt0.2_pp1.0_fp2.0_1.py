import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None
        self.closed = False
    def open(self):
        self.file = open(self.path, self.mode)
    def close(self):
        if self.file:
            self.file.close()
        self.closed = True
    def readable(self):
        return self.mode in ['r', 'r+', 'a+']
    def writable(self):
        return self.mode in ['w', 'w+', 'a', 'a+']
    def seekable(self):
        return True
    def readinto(self, b):
        if not self.file:
            self.open()
        return self.file.readinto(b)
    def read(self, n=-1):
        if not self.file:
            self.open()
        return self.file.read(n)
    def write(self, b):
        if not self.file:
            self.open()
       
