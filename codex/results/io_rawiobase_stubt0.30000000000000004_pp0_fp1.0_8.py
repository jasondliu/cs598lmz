import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        return self.file.close()

class ZipFile(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.zip = zipfile.ZipFile(file)
        self.namelist = self.zip.namelist()
        self.filelist = [self.zip.open(name) for name in self.namelist]
        self.file = self.filelist[0]
        self.index = 0
    def read(self, n=-1):
        if n == -1:
            return self.file.read()
        else:
            return self.file.read(n)
    def seek(self, offset
