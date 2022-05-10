import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
    def read(self, n=-1):
        if n == -1:
            return self.readall()
        if n == 0:
            return b""
        raise NotImplementedError
    def readall(self):
        raise NotImplementedError
    def write(self, b):
        raise NotImplementedError
    def seek(self, offset, whence=io.SEEK_SET):
        raise NotImplementedError
    def tell(self):
        raise NotImplementedError
    def fileno(self):
        raise NotImplementedError
    def flush(self):
        raise NotImplementedError
    def close(self):
        raise NotImplementedError
    def readable(self):
        return "r" in self.mode
    def writable(self):
        return "w" in self.mode
    def seekable(self):
        return True
    def isatty(self):
        return False
   
