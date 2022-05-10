import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.file = open(path, mode)
        self.file_size = os.path.getsize(path)
        self.pos = 0
    def read(self, size):
        self.file.seek(self.pos)
        data = self.file.read(size)
        self.pos += len(data)
        return data
    def tell(self):
        return self.pos
    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = pos
        elif whence == io.SEEK_CUR:
            self.pos += pos
        elif whence == io.SEEK_END:
            self.pos = self.file_size + pos
        else:
            raise ValueError('Invalid whence value')
    def close(self):
        self.file.close()

def get_file_size(path):
    return os.path.getsize(path)

def get_file_content(path):
