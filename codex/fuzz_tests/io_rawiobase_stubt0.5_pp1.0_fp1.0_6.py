import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.length = os.stat(file.name).st_size
        self.offset = 0
    def read(self, size=-1):
        if size == -1:
            self.offset = self.length
            return self.file.read()
        else:
            if self.offset + size > self.length:
                size = self.length - self.offset
            self.offset += size
            return self.file.read(size)
    def tell(self):
        return self.offset
    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.length + offset
        else:
            raise ValueError("Invalid value for whence")
        return self.offset
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return False

