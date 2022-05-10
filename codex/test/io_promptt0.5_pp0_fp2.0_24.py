import io
# Test io.RawIOBase.
class MyRawIOBase(io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        pass
    def write(self, b):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        pass
    def read(self, n=-1):
        pass
    def readall(self):
        pass
    def read1(self, n=-1):
        pass
    def close(self):
        pass
    def fileno(self):
        pass
    def flush(self):
        pass
    def isatty(self):
        pass
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
    def __getstate__(self):
        pass
    def __setstate__(self, state):
        pass

