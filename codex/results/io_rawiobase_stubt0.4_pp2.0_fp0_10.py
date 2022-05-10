import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def readable(self):
        return self.mode[0] in ('r', '+')

    def writable(self):
        return self.mode[0] in ('w', 'a', '+')

    def seekable(self):
        return self.file.seekable()

    def readinto(self, b):
        return self.file.readinto(b)

    def write(self, b):
        return self.file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def flush(self):

