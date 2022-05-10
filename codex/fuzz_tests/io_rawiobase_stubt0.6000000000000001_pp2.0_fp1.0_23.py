import io
class File(io.RawIOBase):
    def __init__(self, url, mode, size):
        self.url = url
        self.mode = mode
        self.size = size
        self.pos = 0
        self.buffer = bytes()

    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = pos
        elif whence == io.SEEK_CUR:
            self.pos += pos
        elif whence == io.SEEK_END:
            self.pos = self.size + pos
        else:
            raise ValueError("invalid value for `whence`")

    def tell(self):
        return self.pos

    def is_open(self):
        return True

    def close(self):
        pass

    def readinto(self, b):
        if self.pos == self.size:
            return 0
        chunk = self.read(len(b))
        b[:len(chunk)] = chunk
        return len(chunk)

    def read(self, size=None):
