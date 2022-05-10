import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None
        self.offset = 0
        self.size = os.path.getsize(path)

    def readinto(self, b):
        if self.file is None:
            self.file = open(self.path, 'rb')
            self.file.seek(self.offset)
        if self.offset >= self.size:
            return 0
        sz = self.file.readinto(b)
        self.offset += sz
        return sz

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.size + offset
        else:
            raise ValueError("Invalid value for `whence`")
        if self.file is not None:
            self.file.close()
            self
