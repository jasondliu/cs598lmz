import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def readable(self):
        return True
    def readinto(self, b):
        n = self.file.readinto(b)
        self.offset += n
        return n
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.file.size() + offset
        else:
            raise ValueError("Invalid whence (%s, should be %d, %d or %d)" % (whence, io.SEEK_SET, io.SEEK_CUR, io.SEEK_END))
        return self.offset
    def tell(self):
        return self.offset
class FileIO(io.IOBase):
    def __init__(
