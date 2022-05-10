import io
class File(io.RawIOBase):
    def __init__(self, path, mode, buffering):
        self.path = path
        self.mode = mode
        self.buffering = buffering
        self.buffer = b''
        self.cursor = 0
    def read(self, size=-1):
        if size < 0:
            return self.readall()
        else:
            if size > len(self.buffer) - self.cursor:
                self.buffer += self.readall()
            r = self.buffer[self.cursor:self.cursor+size]
            self.cursor += size
            return r
    def readall(self):
        return self.path.read(self.buffering)
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.buffer = self.path.read(self.buffering)
            self.cursor = offset
        elif whence == io.SEEK_CUR:
            self.cursor += offset
        elif whence == io.SEEK_END
