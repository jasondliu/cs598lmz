import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.mode = mode
        self.file = None
        self.open(filename, mode)
    def open(self, filename, mode):
        self.file = open(filename, mode)
    def close(self):
        self.file.close()
    def readable(self):
        return self.mode == 'r'
    def writable(self):
        return self.mode == 'w'
    def seekable(self):
        return True
    def readinto(self, b):
        return self.file.readinto(b)
    def write(self, b):
        return self.file.write(b)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def flush(self):
        return self.file.flush()

class FileIO(io.RawIOBase):
    def __init__(self, file, mode):
        self.
