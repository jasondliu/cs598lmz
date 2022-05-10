import io
class File(io.RawIOBase):
    def close(self):
        pass
    def fileno(self):
        return 3
    def isatty(self):
        return True
    def readable(self):
        return True
    def readline(self, size=-1):
        return b''
    def readlines(self, hint=-1):
        return []
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        return 0
    def tell(self):
        return 0
    def truncate(self, pos=None):
        return 0
    def writable(self):
        return True
    def write(self, b):
        return 0

# Classes

class A:
    "A"
    def __init__(self):
        self.v = []
    def __del__(self):
        self.v.clear()
    def __len__(self):
        return len(self.v)
    def __getitem__(self, i):
        return self.v[i]
    def __set
