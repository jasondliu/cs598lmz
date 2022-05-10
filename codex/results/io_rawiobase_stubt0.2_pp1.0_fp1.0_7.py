import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = io.open(name, mode)
        self.size = os.path.getsize(name)
        self.pos = 0
    def read(self, size=-1):
        if size == -1:
            size = self.size - self.pos
        self.file.seek(self.pos)
        self.pos += size
        return self.file.read(size)
    def tell(self):
        return self.pos
    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = pos
        elif whence == io.SEEK_CUR:
            self.pos += pos
        elif whence == io.SEEK_END:
            self.pos = self.size + pos
        else:
            raise ValueError("Invalid value for `whence`")
    def close(self):
        self.file.close()
    def readable(
