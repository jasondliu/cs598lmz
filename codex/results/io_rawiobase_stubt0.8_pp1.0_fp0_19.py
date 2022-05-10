import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n= -1):
        if n >= 0:
            return self.file.read(n)
        else:
            return self.file.read()
    def readall(self):
        return self.file.read()
    def readinto(self, b):
        data = self.file.read(len(b))
        b[:len(data)] = data
        return len(data)
    def write(self, b):
        self.file.write(b)
        return len(b)
    def seek(self, offset, whence = 0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        self.file.flush()
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
import mmap
