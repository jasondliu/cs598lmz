import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.name, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def readinto(self, b):
        return self.file.readinto(b)
    def write(self, b):
        return self.file.write(b)
    def seek(self, pos, whence=io.SEEK_SET):
        return self.file.seek(pos, whence)
    def tell(self):
        return self.file.tell()
    def truncate(self, pos=None):
        return self.file.truncate(pos)
    def flush(self):
        return self.file.flush()
    def fileno(self):
        return self.file.fileno()

f = File
