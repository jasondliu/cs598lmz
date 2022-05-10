import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def readinto(self, b):
        n = self.file.readinto(b)
        self.offset += n
        return n
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.file.size() + offset
        else:
            raise ValueError("Invalid value for `whence`: %r" % (whence,))
        return self.offset
    def tell(self):
        return self.offset
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True

class FileReader(io.BufferedReader):
    def __init__(self, file):
        super().__init__(
