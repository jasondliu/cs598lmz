import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.file = open(path, mode)
        self.size = os.path.getsize(path)
        self.pos = 0
    def read(self, size=-1):
        if size == -1:
            size = self.size - self.pos
        self.pos += size
        return self.file.read(size)
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = self.size + pos
        self.file.seek(self.pos)
    def tell(self):
        return self.pos
    def close(self):
        self.file.close()

class FileReader(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rb')
