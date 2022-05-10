import io
class File(io.RawIOBase):
    def __init__(self, handle):
        self.handle = handle
    def readinto(self, b):
        return self.handle.readinto(b)
    def write(self, b):
        return self.handle.write(b)
    def seek(self, offset, whence=0):
        return self.handle.seek(offset, whence)
    def tell(self):
        return self.handle.tell()
    def read(self, n=-1):
        return self.handle.read(n)
    def readall(self):
        return self.handle.readall()
    def close(self):
        return self.handle.close()
    def readable(self):
        return self.handle.readable()
    def writable(self):
        return self.handle.writable()
    def seekable(self):
        return self.handle.seekable()
    def fileno(self):
        return self.handle.fileno()
    def flush(self):
        return self.handle.flush()

class FileReader(io.BufferedReader):
