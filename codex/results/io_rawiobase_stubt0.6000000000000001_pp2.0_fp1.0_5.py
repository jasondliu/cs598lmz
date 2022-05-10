import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
        self.offset = 0
    def tell(self):
        return self.offset
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.file.seek(0, io.SEEK_END) + offset
        else:
            raise ValueError("Invalid value for whence")
        self.file.seek(self.offset)
        return self.offset
    def readinto(self, buf):
        sz = self.file.readinto(buf)
        self.offset += sz
        return sz
    def read(self, size=-1):
        if size == -1:
            return self.file.read()
        result = self.file.read(size)
        self.offset += len
