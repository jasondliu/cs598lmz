import io
class File(io.RawIOBase):
    def __init__(self, name, mode="r"):
        self.name = name
        self.mode = mode
        self.file = None
    def open(self):
        self.file = open(self.name, self.mode)
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def readable(self):
        return self.mode in ('r', 'w+', 'a+', 'x+')
    def writable(self):
        return self.mode in ('w', 'w+', 'a', 'a+', 'x', 'x+')
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def __enter__
