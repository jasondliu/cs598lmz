import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    def open(self):
        self.file = open(self.filename, self.mode)
    def close(self):
        if self.file:
            self.file.close()
        self.file = None
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return False
    def readinto(self, b):
        return self.file.readinto(b)
    def write(self, b):
        return self.file.write(b)
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)

