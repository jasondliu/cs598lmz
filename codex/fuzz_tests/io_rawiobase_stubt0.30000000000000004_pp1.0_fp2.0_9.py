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
            self.offset = len(self.file) + offset
        else:
            raise ValueError("Invalid value for whence: %r" % (whence,))
    def tell(self):
        return self.offset
    def close(self):
        pass

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if isinstance(file, io.
