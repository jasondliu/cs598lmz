import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode
        self.encoding = 'utf-8'
        self.newlines = None

    def close(self):
        self.file.close()
    def readable(self):
        return self.mode in ('r', 'r+', 'w+', 'a+')
    def writable(self):
        return self.mode in ('w', 'w+', 'a', 'a+')
    def seekable(self):
        return True
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

