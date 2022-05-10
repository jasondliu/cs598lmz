import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = io.open(filename, 'rb')
    def read(self, size=-1):
        return self.file.read(size)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        self.file.close()

class FileStream(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, size=-1):
        return self.file.read(size)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self
