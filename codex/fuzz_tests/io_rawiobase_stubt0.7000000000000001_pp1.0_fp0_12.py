import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.length = os.fstat(file.fileno()).st_size
        self.position = 0
    def tell(self):
        return self.position
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.position = offset
        elif whence == io.SEEK_CUR:
            self.position += offset
        elif whence == io.SEEK_END:
            self.position = self.length + offset
        return self.position
    def read(self, n=-1):
        if self.position >= self.length:
            return b""
        self.file.seek(self.position)
        result = self.file.read(n)
        self.position += len(result)
        return result
    def readable(self):
        return True
    def seekable(self):
        return True

def read_chunks(file, chunk_size=65536):
    while True:
