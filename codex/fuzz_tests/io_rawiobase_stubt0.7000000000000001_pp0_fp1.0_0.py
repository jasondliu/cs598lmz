import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def seekable(self): return True
    def readable(self): return True
    def writable(self): return True
    def read(self, n=-1):
        if n < 0:
            return self.file.read()
        else:
            return self.file.read(n)
    def write(self, b):
        self.file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.file.seek(offset)
        elif whence == io.SEEK_CUR:
            if offset >= 0:
                self.file.seek(self.file.tell() + offset)
            else:
                self.file.seek(self.file.tell() + offset, io.SEEK_SET)
        elif whence == io.SEEK_END:
            self.file.seek(self.file.len + offset, io.SEEK_SET
