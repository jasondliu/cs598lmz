import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def readable(self):
        return True
    def readinto(self, b):
        self.open()
        n = self.file.readinto(b)
        if n is None:
            n = len(b)
        return n
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.open()
        return self.file.seek(offset, whence)
    def tell(self):
        self.open()
        return self.file.tell()
    def writeable(self):
        return True
    def write(self, b):
        self.open()
        return self.file.write(b)
    def open(self):
        if self.file is None:
            self.file = open(self.filename, 'rb')
</code>

