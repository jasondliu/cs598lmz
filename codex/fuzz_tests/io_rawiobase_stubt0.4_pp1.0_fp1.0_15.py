import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, "r+b")
        self.f.seek(0, os.SEEK_END)
        self.size = self.f.tell()
        self.f.seek(0)

    def read(self, size=-1):
        return self.f.read(size)

    def readall(self):
        return self.f.read()

    def seek(self, offset, whence=os.SEEK_SET):
        return self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()

    def write(self, b):
        return self.f.write(b)

    def close(self):
        self.f.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

class FileReader(File):
    def __init__(self, filename):
        super(FileReader, self).__init__(
