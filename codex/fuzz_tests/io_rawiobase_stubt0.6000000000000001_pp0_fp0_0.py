import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readable(self) -> bool:
        return True

    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        b[:n] = data
        self.offset += n
        return n

    def seekable(self) -> bool:
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.file.seek(offset)
        elif whence == io.SEEK_CUR:
            self.file.seek(self.offset+offset)
        elif whence == io.SEEK_END:
            self.file.seek(self.file.size()+offset)
        self.offset = self.file.tell()
        return self.offset

    def tell(self):
        return self.offset

class ZipFile(io.RawIOBase):
    def __init__(self,
