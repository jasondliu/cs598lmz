import io
class File(io.RawIOBase):
    def __init__(self, path, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.path = path
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.close()
    def fileno(self):
        return None
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return False
    def read(self, size=-1):
        return ""
    def read1(self, size=-1):
        return ""
    def readinto(self, b):
        return 0
    def readinto1(self, b):
        return 0
    def write(self, b
