import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, size=-1):
        if size == -1:
            size = os.path.getsize(self.name)
        with open(self.name, 'rb') as f:
            return f.read(size)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        with open(self.name, 'rb') as f:
            f.seek(offset, whence)
    def tell(self):
        with open(self.name, 'rb') as f:
            return f.tell()

class FileWriter(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def write(self, b):
        with open(self.name, 'wb') as f:
            f.write(b)
    def readable(self):
        return False
    def writable
