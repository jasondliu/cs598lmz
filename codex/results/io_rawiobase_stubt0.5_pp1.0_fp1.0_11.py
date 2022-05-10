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
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += self.file.getbuffer().nbytes
        self.offset = offset
        return self.offset

    def tell(self):
        return self.offset

class FileIO(io.IOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        n = self.file.readinto(b)
        self.offset += n
        return n

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.
