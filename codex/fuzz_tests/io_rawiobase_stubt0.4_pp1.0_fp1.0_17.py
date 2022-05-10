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

    def tell(self):
        return self.offset

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.size() + offset
        else:
            raise ValueError("invalid whence (%s, should be 0, 1 or 2)" % whence)
        return self.offset

    def readinto(self, b):
        n = self.file.readinto(b)
        self.offset += n
        return n

    def read(self, n=-1):
        if n >= 0:
            res = self.file.read(n)
        else:
            res = self.file.read()
        self.offset += len(res)
