import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.TextIOBase

class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        return len(b)
    def seek(self, n, whence=0):
        return 0
    def tell(self):
        return 0
    def close(self):
        pass
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True

class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        return len(b)
    def seek(self, n, whence=0):
        return 0
    def tell(self):
        return 0
    def close(self):
        pass
    def readable(self):
        return True
    def writable(self):
        return True
