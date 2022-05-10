import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.file.size + offset
        else:
            raise ValueError("Invalid value for `whence`: %r" % (whence,))
        return self.offset
    def tell(self):
        return self.offset
    def readinto(self, b):
        data = self.file.read(self.offset, len(b))
        b[:len(data)] = data
        self.offset += len(data)
        return len(data)
    def read(self, n=-1):
        data = self.file.read(self
