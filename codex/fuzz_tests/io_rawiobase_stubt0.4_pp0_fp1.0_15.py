import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.path, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def readall(self):
        return self.file.read()
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
    def flush(self):
        return self.file.flush()
    def isatty(self):
        return self.file.isat
