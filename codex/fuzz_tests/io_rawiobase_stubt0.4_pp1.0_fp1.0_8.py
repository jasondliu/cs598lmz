import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None
    def open(self):
        self.file = open(self.file_name, self.mode)
    def close(self):
        self.file.close()
    def read(self, n=-1):
        return self.file.read(n)
    def readinto(self, b):
        return self.file.readinto(b)
    def write(self, b):
        return self.file.write(b)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def fileno(self):
        return self.file.fileno()
    def seekable(self):
        return self.file.seekable()
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
