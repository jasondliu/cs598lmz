import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.handle = None
        self.open()
    def open(self):
        self.handle = open(self.name, 'rb')
    def close(self):
        self.handle.close()
    def readinto(self, buf):
        return self.handle.readinto(buf)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        self.handle.seek(offset, whence)
    def tell(self):
        return self.handle.tell()
    def fileno(self):
        return self.handle.fileno()
    def flush(self):
        self.handle.flush()
    def read(self, n=-1):
        return self.handle.read(n)
    def read1(self, n=-1):
        return self.handle.read1(n)
    def readline(
