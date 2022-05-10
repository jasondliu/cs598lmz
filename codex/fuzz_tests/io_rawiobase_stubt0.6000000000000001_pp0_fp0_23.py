import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = open(name, 'rb')
        self.size = os.fstat(self.file.fileno()).st_size
        self.pos = 0

    def read(self, size=-1):
        if size == -1:
            return self.file.read()
        else:
            return self.file.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
        self.pos = self.file.tell()

    def tell(self):
        return self.pos

class FileSystem:
    def __init__(self, name, base=None):
        self.name = name
        self.base = base
        self.root = self.load(name, base)

    def load(self, name, base):
        return Loader(self, name, base)

    def open(self, path, mode='r', *args, **kwargs):
        return self.root
