import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.file = io.open(filename, 'rb')
        self.len = os.fstat(self.file.fileno()).st_size
        self.offset = 0
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        else:
            assert(False)
    def tell(self):
        return self.offset
    def read(self, amount=None):
        if amount is None:
            amount = self.len - self.offset
        self.file.seek(self.offset)
        data = self.file.read(amount)
        self.offset += len(data)
        return data
    def close(self):
        self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

def read_file_
