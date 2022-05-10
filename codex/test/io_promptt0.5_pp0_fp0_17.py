import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def __init__(self):
        self.file = open("/dev/zero", "rb")
    def read(self, size=-1):
        return self.file.read(size)
    def readinto(self, b):
        return self.file.readinto(b)

# Test io.BufferedIOBase
class BufferedI(io.BufferedIOBase):
    def __init__(self):
        self.file = open("/dev/zero", "rb")
    def read(self, size=-1):
        return self.file.read(size)
    def readinto(self, b):
        return self.file.readinto(b)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()

# Test io.TextIOBase
