import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def __del__(self):
        self.close()
    def readable(self):
        return self.mode in ('r', 'r+', 'w+', 'a+')
    def writable(self):
        return self.mode in ('w', 'w+', 'a', 'a+')
    def seekable(self):
        return self.readable()
    def readinto(self, b):
        return self._readinto(memoryview(b))
    def read(self, n=-1):
        return self.readinto(bytearray(n if n >= 0 else 0))
    def write(self, b):
        return self._write(memoryview(b))
    def fileno(self):
        return self.file.fileno()
    def isatty(self
