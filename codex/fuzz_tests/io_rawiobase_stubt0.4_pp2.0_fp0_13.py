import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None
        self.pos = 0

    def tell(self):
        return self.pos

    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        else:
            raise ValueError("Invalid whence value")

    def read(self, size=-1):
        if size == -1:
            size = None
        if self.file is None:
            self.file = open(self.path, "rb")
            self.file.seek(self.pos)
        data = self.file.read(size)
        self.pos = self.file.tell()
        if not data:
            self.file.close()
            self.file = None
        return data

class FileReader(object):
    def __init__(self, path):
        self.file = File(path)

    def read(self, size=-1):
        return self.file
