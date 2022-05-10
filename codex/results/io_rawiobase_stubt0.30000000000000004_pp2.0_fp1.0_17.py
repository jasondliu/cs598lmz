import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = io.open(path, mode='rb')
        self.size = os.path.getsize(path)
        self.position = 0
    def read(self, size=-1):
        if size == -1:
            size = self.size - self.position
        self.file.seek(self.position)
        data = self.file.read(size)
        self.position += len(data)
        return data
    def tell(self):
        return self.position
    def seek(self, position, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.position = position
        elif whence == io.SEEK_CUR:
            self.position += position
        elif whence == io.SEEK_END:
            self.position = self.size + position
        else:
            raise ValueError('Invalid whence value')
    def close(self):
        self.file.close()

def get_file_size
