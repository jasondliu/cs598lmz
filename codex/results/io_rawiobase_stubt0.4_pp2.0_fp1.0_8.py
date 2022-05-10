import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def read(self, n=-1):
        if not self.file:
            self.file = open(self.filename, 'rb')
        return self.file.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if not self.file:
            self.file = open(self.filename, 'rb')
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
</code>

