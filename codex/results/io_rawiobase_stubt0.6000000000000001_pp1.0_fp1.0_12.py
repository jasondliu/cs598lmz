import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        pass
    def __len__(self):
        return 0
    def __str__(self):
        return ""
    def __repr__(self):
        return ""
    def read(self, size=-1):
        return b""
    def write(self, b):
        return 0
    def close(self):
        pass
    def flush(self):
        pass
    def seek(self, offset, whence=0):
        return 0
    def tell(self):
        return 0
    def readinto(self, b):
        return 0
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def fileno(self):
        return 0
    def isatty(self):
        return False
    def closefd(self):
        pass
    def detach(self):
        return 0
    def read1(self, n):
        return b""
    def truncate(self, size
