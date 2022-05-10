import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.mode = mode
        self.filename = filename
        self.file = None
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def readable(self):
        return 'r' in self.mode
    def writable(self):
        return 'w' in self.mode
    def seekable(self):
        return False
    def readinto(self, b):
        if not self.file:
            self.file = open(self.filename, self.mode)
        return self.file.readinto(b)
    def write(self, b):
        if not self.file:
            self.file = open(self.filename, self.mode)
        return self.file.write(b)

with File('test.txt', 'r') as f:
