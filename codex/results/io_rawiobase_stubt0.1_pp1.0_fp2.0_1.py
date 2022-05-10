import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        self.file.close()

class FileReader(File):
    def __init__(self, file):
        super().__init__(file)
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        self.file.close()

class FileWriter(File):
    def __init__(self, file):
        super().__init__(file)
        self.file = file
