import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        if mode != 'r':
            raise IOError('Read only')
        self.fp = open(path, 'rb')
        self.size = os.fstat(self.fp.fileno()).st_size
        self.offset = 0
    def read(self, n):
        if self.offset >= self.size:
            return b''
        self.fp.seek(self.offset)
        data = self.fp.read(n)
        self.offset += len(data)
        return data
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.size + offset
    def tell(self):
        return self.offset

class File_:
    def __init__(self
