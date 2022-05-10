import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def read(self, n=-1):
        if self.file is None:
            self.file = open(self.filename, 'rb')
        return self.file.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if self.file is None:
            self.file = open(self.filename, 'rb')
        return self.file.seek(offset, whence)
    def tell(self):
        if self.file is None:
            self.file = open(self.filename, 'rb')
        return self.file.tell()
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def __del__(self):
        self.close()

class FileWrapper(io.RawIOBase):
    def __init__(self, file):

