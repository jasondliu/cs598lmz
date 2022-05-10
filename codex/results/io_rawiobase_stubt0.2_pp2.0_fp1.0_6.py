import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None
    def open(self):
        self.file = open(self.path, 'rb')
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class FileReader(File):
    def __init__(self, path):
        super().__init__(path)
        self.open()
    def read(self, size=-1):
        return self.file.read(size)
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
   
