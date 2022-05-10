import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rb')
        self.size = os.path.getsize(path)
        self.pos = 0
        self.closed = False

    def read(self, size=-1):
        if size == -1:
            size = self.size - self.pos
        if size == 0:
            return b''
        self.file.seek(self.pos)
        data = self.file.read(size)
        self.pos += len(data)
        return data

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = offset
        elif whence == io.SEEK_CUR:
            self.pos += offset
        elif whence == io.SEEK_END:
            self.pos = self.size + offset
        else:
            raise ValueError('Invalid whence value')

    def tell(self):
        return self.pos

    def close(self):
