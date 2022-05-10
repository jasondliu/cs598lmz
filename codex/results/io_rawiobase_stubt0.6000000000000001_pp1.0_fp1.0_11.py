import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def fileno(self):
        return self.file.fileno()
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def readinto(self, b):
        return self.file.readinto(b)
    def readall(self):
        return self.file.readall()
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        return self.file.write(b)
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seekable(self):
        return self.file.seekable()
    def close(self):
        self.file.close()
    def detach(self):
        return self.file.
