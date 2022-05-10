import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.f = io.open(self.path, self.mode)
        self.size = os.path.getsize(self.path)
        self.pos = 0

    def read(self, size=-1):
        if size == -1:
            self.pos = self.size
            return self.f.read(self.size)
        else:
            self.pos += size
            return self.f.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = offset
            self.f.seek(offset)
        elif whence == io.SEEK_CUR:
            self.pos += offset
            self.f.seek(self.pos)
        elif whence == io.SEEK_END:
            self.pos = self.size + offset
            self.f.seek(self.pos)
        return self.pos

   
