import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.length = os.fstat(file.fileno()).st_size
        self.position = 0
    def read(self, size=-1):
        if size == -1:
            size = self.length - self.position
        self.file.seek(self.position)
        data = self.file.read(size)
        self.position += len(data)
        return data
    def readinto(self, b):
        data = self.read(len(b))
        if not data:
            return None
        b[:len(data)] = data
        return len(data)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 0:
            self.position = offset
        elif whence == 1:
            self.position += offset
        elif whence == 2:
            self.position = self.length + offset
    def tell(self):
        return self.position
    def readable(self):
