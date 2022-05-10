import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rb')
        self.size = os.fstat(self.file.fileno()).st_size
        self.position = 0
    def read(self, size=-1):
        if size == -1:
            size = self.size - self.position
        if size == 0:
            return b''
        data = self.file.read(size)
        self.position += len(data)
        return data
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.position = offset
        elif whence == io.SEEK_CUR:
            self.position += offset
        elif whence == io.SEEK_END:
            self.position = self.size + offset
        else:
            raise ValueError('Invalid value for whence: {}'.format(whence))
        self.file.seek(self.position, io.SEEK_SET)
    def tell(
