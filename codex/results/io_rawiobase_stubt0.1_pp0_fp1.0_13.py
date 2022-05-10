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
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = len(self.file) + offset
        else:
            raise ValueError("Invalid value for `whence`")
        return self.offset
    def tell(self):
        return self.offset
    def readinto(self, b):
        n = len(b)
        if self.offset + n > len(self.file):
            n = len(self.file) - self.offset
        b[:n] = self.file[self.offset:self.offset+n]
        self.offset
