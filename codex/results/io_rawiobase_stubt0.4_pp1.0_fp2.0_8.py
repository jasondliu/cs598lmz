import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()

class ZipFile(File):
    def __init__(self, file):
        super().__init__(file)
        self.zfile = zipfile.ZipFile(file)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
    def close(self):
        self.zfile.close()
    def read(self, n=-1):
        return self.zfile.read(n)
    def seek(self, offset, whence=0):
        self.zfile.seek(offset, whence)
    def tell(self):
        return self.
