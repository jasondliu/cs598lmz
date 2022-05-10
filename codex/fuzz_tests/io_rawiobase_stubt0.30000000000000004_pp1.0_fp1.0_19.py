import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"\x00"*n
    def write(self, b):
        return len(b)
    def readinto(self, b):
        return len(b)
    def readall(self):
        return b""
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def truncate(self, size=None):
        pass
    def flush(self):
        pass
    def close(self):
        pass
    def fileno(self):
        return -1
    def isatty(self):
        return False
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True

