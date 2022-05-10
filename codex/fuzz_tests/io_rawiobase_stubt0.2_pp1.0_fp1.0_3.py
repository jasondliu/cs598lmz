import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def readable(self):
        return True
    def readinto(self, b):
        i = self.file.readinto(b)
        self.offset += i
        return i
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += self.file.size()
        self.offset = offset
        return self.offset
    def tell(self):
        return self.offset
    def writable(self):
        return True
    def write(self, b):
        i = self.file.write(b)
        self.offset += i
        return i

def open(file, *args, **kwargs):
    return io.open(File(file), *args, **kwargs)

def test():
    import uio

