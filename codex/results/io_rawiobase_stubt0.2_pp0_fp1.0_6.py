import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return False
    def readinto(self, b):
        n = self.file.readinto(b)
        self.offset += n
        return n
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
    def close(self):
        self.file.close()

class FileWrapper:
    def __init__(self, file):
