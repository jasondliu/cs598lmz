import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.pos = 0
        self.open(filename, mode)

    def open(self, filename, mode):
        if self.file:
            self.file.close()
        self.file = open(filename, mode)
        self.pos = self.file.tell()

    def close(self):
        self.file.close()

    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = pos
        elif whence == io.SEEK_CUR:
            self.pos += pos
        elif whence == io.SEEK_END:
            self.pos = self.size() + pos
        else:
            raise ValueError("Invalid value for `whence`")

        self.file.seek(self.pos)

    def tell(self):
        return self.pos

    def read(self, size=-1):
        data
