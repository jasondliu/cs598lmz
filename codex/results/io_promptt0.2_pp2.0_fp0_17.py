import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'abc'
    def write(self, b):
        return len(b)
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self, offset, whence=0):
        return 0
    def tell(self):
        return 0
    def close(self):
        pass

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'abc'
    def write(self, b):
        return len(b)
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self, offset, whence=0):
        return 0
    def tell(self):
        return 0
    def close(self):
        pass

# Test io
