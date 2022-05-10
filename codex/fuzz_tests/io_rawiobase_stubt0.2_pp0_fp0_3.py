import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        return self.file.close()
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return False

class BytesIO(io.BytesIO):
    def __init__(self, initial_bytes=None):
        io.BytesIO.__init__(self, initial_bytes)
    def read(self, n=-1):
        return io.BytesIO.read(self, n)
    def seek(self, offset, whence=0):
        return io.BytesIO.seek(self, offset, whence)
    def tell(self):
        return io.BytesIO.tell(self)
    def close(self
