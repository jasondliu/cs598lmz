import io
# Test io.RawIOBase
encoded = """\
qwertyuiop
asdfghjkl
"""
buf = io.BytesIO(encoded.encode('utf8'))

class UTF8IOWrapper(io.RawIOBase):

    def __init__(self, buffer):
        self.buffer = buffer

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return self.buffer.readinto(b)

    def write(self, b):
        return self.buffer.write(b)

    def readinto1(self, b):
        return self.buffer.readinto1(b)

    def readall(self):
        return self.buffer.readall()

    def read(self, size=-1):
        return self.buffer.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.buffer.seek(offset, whence)

    def tell(self):
        return self
