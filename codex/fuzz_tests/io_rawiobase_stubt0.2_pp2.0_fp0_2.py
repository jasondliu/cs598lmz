import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return False

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.file.size + offset
        else:
            raise ValueError("Invalid value for whence")

    def tell(self):
        return self.offset

    def readinto(self, b):
        self.file.readinto(b, self.offset)
        self.offset += len(b)
        return len(b)

    def read(self, n=-1):
        if n == -1:
            n = self.file.size - self.offset
        b = bytearray(n)
        self.readinto(b)
        return bytes(b)

    def write
