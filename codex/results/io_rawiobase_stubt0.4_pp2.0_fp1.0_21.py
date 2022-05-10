import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def read(self, n=-1):
        self.file.seek(self.offset)
        s = self.file.read(n)
        self.offset = self.file.tell()
        return s
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.file.size + offset
        else:
            raise ValueError("whence must be io.SEEK_SET, io.SEEK_CUR, or io.SEEK_END")
    def tell(self):
        return self.offset

class FileReader(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def read(self, n=-
