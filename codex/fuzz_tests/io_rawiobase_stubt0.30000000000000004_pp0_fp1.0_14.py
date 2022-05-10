import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = open(path, "rb")
        self.size = os.path.getsize(path)
        self.offset = 0
    def readinto(self, b):
        if self.offset >= self.size:
            return 0
        size = len(b)
        if self.offset + size > self.size:
            size = self.size - self.offset
        self.file.seek(self.offset)
        self.offset += size
        return self.file.readinto(b[:size])
    def close(self):
        self.file.close()
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.size + offset
        else:
            raise ValueError("Invalid whence")
       
