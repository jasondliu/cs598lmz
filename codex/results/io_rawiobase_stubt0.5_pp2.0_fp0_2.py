import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = os.open(name, os.O_RDONLY)
        self.size = os.fstat(self.fd).st_size
        self.pos = 0
    def tell(self):
        return self.pos
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = offset
        elif whence == io.SEEK_CUR:
            self.pos += offset
        elif whence == io.SEEK_END:
            self.pos = self.size + offset
        else:
            raise ValueError('invalid whence')
        return self.pos
    def read(self, n):
        if n > 0:
            data = os.read(self.fd, n)
            self.pos += len(data)
            return data
        else:
            return b''
    def readall(self):
        return self.read(self.size)
    def close(self
